from datetime import date

from fastapi import APIRouter
from sqlalchemy.exc import SQLAlchemyError

from app.hotels.dao import HotelsDAO
from app.hotels.schemas import SHotelInfo, SHotels
from app.logger import logger

router = APIRouter(
    prefix='/hotels',
    tags=['Отели'],
)


@router.get('/{hotel_location}')
async def get_hotels_by_location(hotel_location: str,
                                 date_from: date,
                                 date_to: date) -> list[SHotelInfo] | None:
    try:
        hotels = await HotelsDAO.find_by_location(hotel_location, date_from=date_from, date_to=date_to)
        return hotels
    except (SQLAlchemyError, Exception):
        extra = {
            "hotel_location": hotel_location
        }
        logger.error(msg='Ошибка при бронирование', extra=extra, exc_info=True)


@router.get('/id/{hotel_id}')
async def get_hotel_byt_id(hotel_id: int) -> SHotels | None:
    try:
        return await HotelsDAO.find_all(id=hotel_id)
    except (SQLAlchemyError, Exception):
        extra = {
            "hotel_id": hotel_id
        }
        logger.error(msg='Ошибка при бронирование', extra=extra, exc_info=True)
