from typing import TYPE_CHECKING

import sqlalchemy
from sqlalchemy.dialects.postgresql import BYTEA, INTEGER
from sqlalchemy import String, Text, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .products import Product
#     from .sd_run_post import SD_run_post
#     from .sd_token import SDToken


class Categorie(Base):
    name: Mapped[str] = mapped_column(String(30), unique=False)
    description: Mapped[str] = mapped_column(String(300), unique=False)

    product: Mapped[list["Product"]] = relationship(back_populates="category", cascade="all, delete")

