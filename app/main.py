import time
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from sqladmin import Admin

from app.admin.auth import authentication_backend
from app.admin.views import BookingsAdmin, HotelsAdmin, RoomsAdmin, UsersAdmin
from app.bookings.router import router as router_bookings
from app.config import settings
from app.database import engine
from app.hotels.rooms.router import router as router_rooms
from app.hotels.router import router as router_hotels
from app.images.router import router as router_images
from app.importer.router import router as router_importer
from app.logger import logger
from app.pages.router import router as router_pages
from app.users.router import router as router_users

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}")
    FastAPICache.init(RedisBackend(redis), prefix="cache")
    yield


app.mount('/static', StaticFiles(directory='app/static'), 'static')
app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_hotels)
app.include_router(router_rooms)
app.include_router(router_pages)
app.include_router(router_images)
app.include_router(router_importer)


origins = [
    'http://localhost:8000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'OPTIONS', 'DELETE', 'PATCH', 'PUT'],
    allow_headers=['Content-Type', 'Set-Cookie', 'Access-Control-Allow-Headers', 'Access-Control-Allow-Origin',
                   'Authorization']
)


admin = Admin(app, engine, authentication_backend=authentication_backend)
admin.add_view(UsersAdmin)
admin.add_view(HotelsAdmin)
admin.add_view(BookingsAdmin)
admin.add_view(RoomsAdmin)

@app.middleware('http')
async def add_process_time_header(requset: Request, call_next):
    start_time = time.time()
    response = await call_next(requset)
    process_time = time.time() - start_time
    logger.info('Request excute time', extra={
        'process time': round(process_time, 4)
    })
    return response
