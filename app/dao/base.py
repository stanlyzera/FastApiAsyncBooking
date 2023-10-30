from sqlalchemy import delete, insert, select

from app.database import async_session_maker


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
