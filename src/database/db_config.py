from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import Request


SQLALCHEMY_DATABASE_URI = "sqlite:///./sql_app.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit= False, autoflush=False, bind= engine)
Base = declarative_base()


#Dependency
def get_db_connection(request: Request):
    return request.state.db