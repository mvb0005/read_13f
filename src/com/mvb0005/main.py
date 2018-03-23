from sqlalchemy.orm import sessionmaker

import com.mvb0005.database.database_setup
from com.mvb0005.asset import Asset
from com.mvb0005.information import Information
import com.mvb0005.Scraper as scraper

engine = com.mvb0005.database.database_setup.setup()
Session = sessionmaker(bind=engine)
session = Session(bind=engine)

for n in range(10):
    infolist = scraper.get_information_table_links_from_url(scraper.sec_url, n)
    for info in infolist:
        i = Information(info)
        if session.query(Information).filter(Information.cik == info[0]).count() == 0:
            session.add(i)
            session.commit()
        if session.query(Asset).filter(Asset.cik == i.cik).count() == 0:
            print(i)
            asset_list = scraper.get_asset_table_from_information(i)
            for x in asset_list:
                print(x.cusip)
                try:
                    session.add(x)
                    session.commit()
                except Exception:
                    pass


session.close()




