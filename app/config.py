from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MODE: Literal['DEV', 'TEST', 'PROD']
    LOG_LEVEL: Literal['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASS: str

    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASS: str

    AUTH_KEY: str
    AUTH_ALGO: str

    REDIS_HOST: str
    REDIS_PORT: int

    SENTRY_DSN: str

    @property
    def DATABASE_URL(self):
        user = f'{self.DB_USER}:{self.DB_PASS}'
        database = f'{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        return f'postgresql+asyncpg://{user}@{database}'

    TEST_DB_HOST: str
    TEST_DB_PORT: int
    TEST_DB_NAME: str
    TEST_DB_USER: str
    TEST_DB_PASS: str

    @property
    def TEST_DATABASE_URL(self):
        user = f'{self.TEST_DB_USER}:{self.TEST_DB_PASS}'
        database = f'{self.TEST_DB_HOST}:{self.TEST_DB_PORT}/{self.TEST_DB_NAME}'
        return f'postgresql+asyncpg://{user}@{database}'

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
