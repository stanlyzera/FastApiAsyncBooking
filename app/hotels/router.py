from datetime import date

from fastapi import APIRouter

from app.hotels.dao import HotelsDAO
from app.hotels.schemas import SHotelInfo, SHotels

router = APIRouter(
    prefix='/hotels',
    tags=['Отели'],
)


@router.get('/{hotel_location}')
async def get_hotels_by_location(hotel_location: str,
                                 date_from: date,
                                 date_to: date) -> list[SHotelInfo]:
    hotels = await HotelsDAO.find_by_location(hotel_location, date_from=date_from, date_to=date_to)
    return hotels


@router.get('/id/{hotel_id}')
async def get_hotel_byt_id(hotel_id: int) -> SHotels:
    return await HotelsDAO.find_all(id=hotel_id)
