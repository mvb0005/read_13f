import urllib.request
import bs4 as bs
import re

import time

sec_url = "https://searchwww.sec.gov/EDGARFSClient/jsp/EDGAR_MainAccess.jsp?search_text=INFORMATION%20TABLE&sort=Date" \
          "&formType=Form13FHR&isAdv=true&stemming=true&numResults=10&numResults=10 "


def make_web_call_with_delay(u):
    time.sleep(.5)
    return urllib.request.urlopen(u)


def get_information_table_links_from_url(url):
    global filing
    source = make_web_call_with_delay(url)
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
    dates = soup.find_all('i', class_='blue')
    ciks = [x.text for x in soup.find_all('a', id="cikSearch")]
    assert len(ciks) == len(dates) == len(infotable_xml_links), "ciks to dates to links is not a 1:1:1 ratio"
    return zip(ciks, dates, infotable_xml_links)


print(get_information_table_links_from_url(sec_url))
