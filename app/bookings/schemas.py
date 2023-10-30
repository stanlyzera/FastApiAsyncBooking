from datetime import date
from typing import List

from pydantic import BaseModel


class SBooking(BaseModel):
    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int


class SBookingWRoom(SBooking):
    image_id: int
    name: str
    description: str
    services: List[str]
