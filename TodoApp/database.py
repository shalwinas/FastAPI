from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# SQLALCHEMY_DATABASE_URL = "sqlite:///./todosapp.db" # 1. create a loc in our fastapi app ---for SQLITE3
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False})

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg://postgres:gpWSHQogqJEjyvGJ@db.uxkafvxuascomhrezvhq.supabase.co:5432/postgres"# 1. create a loc in our fastapi app
# postgresql://postgres:gpWSHQogqJEjyvGJ@db.uxkafvxuascomhrezvhq.supabase.co:5432/postgres

#2. create engine
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}) #conn arg allowes us to check  ---for SQLITE3
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#3. sessionlocal
SessionLocal = sessionmaker(autocommit= False, autoflush= False, bind= engine)

#4. base ---object of the database -- to control database
Base = declarative_base()