import urllib.request
import bs4 as bs
import re
from com.mvb0005.information import Information
from com.mvb0005.asset import Asset

import time

sec_url = "https://searchwww.sec.gov/EDGARFSClient/jsp/EDGAR_MainAccess.jsp?search_text=INFORMATION+TABLE&sort=Date" \
          "&startDoc={}1&numResults=10&isAdv=true&formType=Form13FHR&fromDate=mm/dd/yyyy&toDate=mm/dd/yyyy&stemming" \
          "=false "


def make_web_call_with_delay(u):
    time.sleep(.5)
    return urllib.request.urlopen(u)


def get_information_table_links_from_url(url, n):
    source = make_web_call_with_delay(url.format(n))
    soup = bs.BeautifulSoup(source, 'lxml')
    filings = soup.find_all('a', class_='filing')
    infotable_xml_links = []
    for filing in filings:
        try:
            link = re.findall("opennew\(\'(.*?)\'", str(filing))[0]
            infotable_xml_links.append(link)
        except IndexError():
            print(f"link not found in: {filing}")
            raise
    dates = [x.text for x in soup.find_all('i', class_='blue')]
    ciks = [x.text for x in soup.find_all('a', id="cikSearch")]
    assert len(ciks) == len(dates) == len(infotable_xml_links), "ciks to dates to links is not a 1:1:1 ratio"
    return zip(ciks, dates, infotable_xml_links)

def get_asset_table_from_information(information):
    source = make_web_call_with_delay(information.url)
    soup = bs.BeautifulSoup(source, 'lxml')
    assets = [x for x in soup.find_all("tr") if (x.find("td", class_="FormData") is not None)]
    assetlist = []
    for asset in assets:
        asset_table = [x.text for x in asset.find_all("td")]
        asset_table = asset_table[:5] + [asset_table[7]]
        newasset = Asset()
        newasset.set_share_info(asset_table)
        newasset.set_cik_date(information.cik, information.date)
        assetlist.append(newasset)
    return assetlist


url = "https://www.sec.gov/Archives/edgar/data/1732846/000173284618000001/xslForm13F_X01/indew4q17.xml"
o = Information(0, 0, url)
get_asset_table_from_information(o)

