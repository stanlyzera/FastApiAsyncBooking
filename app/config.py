from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASS: str

    @property
    def DATABASE_URL(self):
        user = f'{self.DB_USER}:{self.DB_PASS}'
        database = f'{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        return f'postgresql+asyncpg://{user}@{database}'

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

print(settings.DATABASE_URL)
