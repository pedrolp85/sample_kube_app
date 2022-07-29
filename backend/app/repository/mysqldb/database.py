from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os

database_host = os.environ['DATABASE_HOST']
database_port = os.environ.get("DATABASE_PORT", "3306")
database_password = os.environ['DATABASE_PASSWORD']
database_user = os.environ['DATABASE_USER']
database_schema = os.environ['DATABASE_SCHEMA']

SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{database_user}:{database_password}@{database_host}:{database_port}/{database_schema}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
