from pathlib import Path
from pydantic import BaseModel
from dotenv import load_dotenv
import os


# load_dotenv()
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent
load_dotenv()

class DbSettings(BaseModel):
    username: str = os.getenv("DATABASE_USER")
    password: str = os.getenv("DATABASE_PASSWORD")
    host: str = os.getenv("DATABASE_HOST")
    name: str = os.getenv("DATABASE_NAME")
    echo: bool = False

    @property
    def url(self) -> str:
        return f"postgresql+asyncpg://{self.username}:{self.password}@db:1212/{self.name}"


class Settings(BaseSettings):
    db: DbSettings = DbSettings()



settings = Settings()