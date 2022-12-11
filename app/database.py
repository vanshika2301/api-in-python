from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#in case if you dont want to use sqlalchemy you can use postgresql driver PSYCOPG2 to connect to your database.
#import psycopg2
#from psycopg2.extras import RealDictCursor
#while True:
    #try:
        #conn = psycopg2.connect(host=settings.database_hostname, database=settings.database_name, user=settings.database_username, password=settings.database_password, cursor_factory=RealDictCursor)
        #cursor = conn.cursor()
        #print('Database connection was successfull!')
        #break
    #except Exception as error:
        #print('Connecting to database failed')
        #print('Error: ', error)
        #time.sleep(2)