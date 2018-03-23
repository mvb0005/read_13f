from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


def setup():
    engine = create_engine('sqlite:///database/test.db')
    Base.metadata.create_all(bind=engine)
    return engine
