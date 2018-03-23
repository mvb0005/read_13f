from sqlalchemy import Column, String
from com.mvb0005.database.database_setup import Base

class Information(Base):
    __tablename__ = "information_table"

    cik = Column("cik", String, primary_key=True)
    date = Column("date", String)
    url = Column("url", String)

    def __init__(self, *args, **kwargs):
        if len(args) == 3:
            self.cik = args[0]
            self.date = args[1]
            self.url = args[2]

        if len(args) == 1:
            list_with_cik_date_url = args[0]
            self.cik = list_with_cik_date_url[0]
            self.date = list_with_cik_date_url[1]
            self.url = list_with_cik_date_url[2]


