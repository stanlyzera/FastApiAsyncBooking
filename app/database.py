from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True)

async_session_maker = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)  # type: ignore


class Base(DeclarativeBase):
    pass
