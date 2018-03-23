from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class Asset(Base):
    __tablename__ = "asset"

    cik = Column("cik", String, primary_key=True)
    name = Column("name", String)
    date = Column("date", String)
    title = Column("title", String)
    cusip = Column("cusip", String, primary_key=True)
    cash_value = Column("cash_value", String)
    num_shares = Column("num_shares", String)
    type = Column("type", String)
    discretion = Column("discretion", String)


class InformationTable(Base):
    __tablename__ = "information_table"

    cik = Column("cik", String, primary_key=True)
    date = Column("date", String)
    url = Column("url", String)

    def __init__(self, cik_, date_, url_):
        self.cik = cik_
        self.date = date_
        self.url = url_


engine = create_engine('sqlite:///test.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()
asset = Asset()
asset.cik = "123457"
asset.name = "Ben"

session.add(asset)
session.commit()

session.close()
