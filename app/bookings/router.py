from datetime import date

from fastapi import APIRouter, Depends
from pydantic import TypeAdapter

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBookingWRoom, SNewBooking
from app.tasks.tasks import send_booking_confirmation_email
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix='/bookings',
    tags=['Бронирование'],
)


@router.get('')
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBookingWRoom]:
    return await BookingDAO.get_user_booking(user)


@router.post('')
async def add_booking(
    room_id: int,
    date_from: date,
    date_to: date,
    user: Users = Depends(get_current_user)
) -> None:
    booking = await BookingDAO.add(user.id, room_id, date_from, date_to)
    booking = TypeAdapter(SNewBooking).validate_python(booking).model_dump()
    send_booking_confirmation_email.delay(booking, user.email)


@router.delete("/{booking_id}", status_code=204)
async def remove_booking(
    booking_id: int,
    current_user: Users = Depends(get_current_user),
) -> None:
    await BookingDAO.delete(id=booking_id, user_id=current_user.id)