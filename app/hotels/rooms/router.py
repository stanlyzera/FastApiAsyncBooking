from datetime import date

from fastapi import APIRouter

from app.hotels.rooms.dao import RoomsDAO
from app.hotels.rooms.schemas import SRoomInfo

router = APIRouter(
    prefix='/hotels',
    tags=['Комнаты'],
)


@router.get('/{hotel_id}/rooms')
async def get_hotels_rooms(hotel_id: int,
                           date_from: date,
                           date_to: date) -> SRoomInfo:
    hotels = await RoomsDAO.find_rooms(hotel_id=hotel_id, date_from=date_from, date_to=date_to)
    return hotels
