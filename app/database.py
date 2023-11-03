from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings

if settings.MODE == 'TEST':
    DATABASE = settings.TEST_DATABASE_URL
    DATABASE_PARAMS = {'poolclass': NullPool}
else:
    DATABASE = settings.DATABASE_URL
    DATABASE_PARAMS = {}

engine = create_async_engine(DATABASE, echo=False, **DATABASE_PARAMS)

async_session_maker = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession)  # type: ignore


class Base(DeclarativeBase):
    pass
