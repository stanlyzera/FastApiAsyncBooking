from datetime import datetime

from fastapi import Depends, Request
from jose import JWTError, jwt

from app.config import settings
from app.exceptions import (IncorrectTokenFormatException,
                            TokenAbsentException, TokenExpiredException,
                            UserIsNotExistException)
from app.users.dao import UserDAO


def get_token(request: Request):
    token = request.cookies.get('booking_access_token')
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.AUTH_KEY, settings.AUTH_ALGO
        )
    except JWTError:
        raise IncorrectTokenFormatException
    expire = payload.get('exp')
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpiredException
    user_id = payload.get('sub')
    if not user_id:
        raise UserIsNotExistException
    user = await UserDAO.find_one_or_none(id=int(user_id))
    if not user:
        raise UserIsNotExistException

    return user
