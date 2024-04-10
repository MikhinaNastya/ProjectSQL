from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine(
    "postgresql+psycopg2://postgres:123456mav@localhost/python17_2",
    echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()