from fastapi import APIRouter

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking

router = APIRouter(
    prefix='/bookings',
    tags=['Бронирование'],
)


@router.get('')
async def get_bookings() -> list[SBooking]:
    result = await BookingDAO.find_all()
    return result
