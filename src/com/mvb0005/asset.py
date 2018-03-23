from sqlalchemy import Column, String
from com.mvb0005.database.database_setup import Base

class Asset(Base):
    __tablename__ = "asset_table"
    cik = Column("cik", String, primary_key=True)
    name = Column("name", String)
    date = Column("date", String, primary_key=True)
    title = Column("title", String)
    cusip = Column("cusip", String, primary_key=True)
    cash_value = Column("cash_value", String)
    num_shares = Column("num_shares", String)
    type = Column("type", String)
    discretion = Column("discretion", String)

    def set_share_info(self, infolist):
        self.name = infolist[0]
        self.type = infolist[1]
        self.cusip = infolist[2]
        self.cash_value = infolist[3]
        self.num_shares = infolist[4]
        self.discretion = infolist[5]

    def set_cik_date(self, cik, date):
        self.cik = cik
        self.date = date



