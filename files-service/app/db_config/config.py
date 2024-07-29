import logging

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from ..config import config

logger = logging.getLogger(__name__)

Base = declarative_base()

engine = create_engine(
    # need to figure out these settings
    # DATABASE_URL, echo=True, connect_args={"check_same_thread": False}
    config.DB_CONFIG
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Database:
    def __init__(self):
        self.__session = None
        self.__engine = None

    def connect(self, db_config):
        self.__engine = create_async_engine(
            config.DB_CONFIG,
        )

        self.__session = async_sessionmaker(
            bind=self.__engine,
            autocommit=False,
        )

    async def disconnect(self):
        await self.__engine.dispose()

    async def get_db(self):
        async with self.__session() as session:
            yield session


db = Database()