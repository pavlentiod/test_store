from typing import TYPE_CHECKING

import sqlalchemy
from sqlalchemy.dialects.postgresql import BYTEA, INTEGER
from sqlalchemy import String, Text, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .categories import Categorie
#     from .sd_run_post import SD_run_post
#     from .sd_token import SDToken


class Product(Base):
    name: Mapped[str] = mapped_column(String(30), unique=False)
    description: Mapped[str] = mapped_column(String(300), unique=False)
    price: Mapped[int] = mapped_column(INTEGER, nullable=False)
    weight: Mapped[int] = mapped_column(INTEGER, nullable=False)

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    category: Mapped["Categorie"] = relationship(back_populates="product")
