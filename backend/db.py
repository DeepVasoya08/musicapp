from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = "postgresql://postgre:password@localhost/db"

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False, bind=engine)

Base = declarative_base()
