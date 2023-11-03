from sqlalchemy import delete, insert, select
from sqlalchemy.exc import SQLAlchemyError

from app.database import async_session_maker
from app.logger import logger


class BaseDAO:
    model = None

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:  # type: ignore
            query = select(cls.model.__table__.columns).filter_by(
                **filter_by)  # type: ignore
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:  # type: ignore
            query = select(cls.model.__table__.columns).filter_by(
                **filter_by)  # type: ignore
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:  # type: ignore
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete(cls, **filter_by):
        async with async_session_maker() as session:  # type: ignore
            query = delete(cls.model).filter_by(**filter_by)
            await session.execute(query)
            await session.commit()
            
    @classmethod
    async def add_bulk(cls, *data):
        try:
            query = insert(cls.model).values(*data).returning(cls.model.id)
            async with async_session_maker() as session: # type: ignore
                result = await session.execute(query)
                await session.commit()
                return result.mappings().first()
        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg = "Database Exc"
            elif isinstance(e, Exception):
                msg = "Unknown Exc"

            logger.error(msg, extra={"table": cls.model.__tablename__}, exc_info=True)
            return None
