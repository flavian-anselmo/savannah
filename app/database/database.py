from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.config.config import settings



SQLALCHEMY_DATABASE_URL =  f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_host}/{settings.database_name}'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# dependancy 
def get_db():
    '''
    database dependancy for any endpont making a query to the db 
    
    '''
    db:sessionmaker = SessionLocal()
    try:
        yield db 

    finally:
        db.close() 