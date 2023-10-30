
from datetime import date

from sqlalchemy import and_, func, or_, select

from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.hotels.rooms.models import Rooms


class RoomsDAO(BaseDAO):
    model = Rooms

    @classmethod
    async def find_rooms(cls, hotel_id: int, date_from: date, date_to: date):
        rooms_booked = (
            select(Bookings.room_id, func.count(Bookings.room_id).label('booked_rooms')).where(
                or_(
                    and_(
                        Bookings.date_from >= date_from,
                        Bookings.date_from <= date_to,
                    ),
                    and_(
                        Bookings.date_from <= date_from,
                        Bookings.date_to > date_from,
                    ),
                ),
            )
        ).group_by(Bookings.room_id).cte('rooms_booked')
        result = (
            select(Rooms.__table__.columns,
                   (Rooms.price * (date_to - date_from).days).label('total_cost'),
                   (Rooms.quantity - func.coalesce(rooms_booked.c.booked_rooms, 0)
                    ).label("rooms_left")
                   ).join(rooms_booked, rooms_booked.c.booked_rooms == Rooms.id, isouter=True).where(
                Rooms.hotel_id == hotel_id
            )
        )
        async with async_session_maker() as session:  # type: ignore
            rooms_in_hotel = await session.execute(result)
            return rooms_in_hotel.mappings().all()