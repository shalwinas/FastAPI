from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# SQLALCHEMY_DATABASE_URL = "sqlite:///./todosapp.db" # 1. create a loc in our fastapi app ---for SQLITE3
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False})

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg://postgres.uxkafvxuascomhrezvhq:gpWSHQogqJEjyvGJ@aws-0-ap-south-1.pooler.supabase.com:6543/postgres"# 1. create a loc in our fastapi app
# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg://postgres:swn2001@localhost:5432/postgres"# 1. create a loc in our fastapi app


#2. create engine
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}) #conn arg allowes us to check  ---for SQLITE3
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#3. sessionlocal
SessionLocal = sessionmaker(autocommit= False, autoflush= False, bind= engine)

#4. base ---object of the database -- to control database
Base = declarative_base()