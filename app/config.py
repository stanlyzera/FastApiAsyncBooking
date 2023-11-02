from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
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

    @property
    def DATABASE_URL(self):
        user = f'{self.DB_USER}:{self.DB_PASS}'
        database = f'{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        return f'postgresql+asyncpg://{user}@{database}'

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
