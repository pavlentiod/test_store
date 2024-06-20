from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, EmailStr, ConfigDict



class ProductCreate(BaseModel):
    name: Annotated[str, MinLen(2), MaxLen(30)]
    description: Annotated[str, MinLen(2)]
    price: int
    weight: int
    category_id: int = 1


class ProductUpdate(BaseModel):
    name: Annotated[str, MinLen(2), MaxLen(30)] = None
    description: Annotated[str, MinLen(2)] = None
    price: int = None
    weight: int = None
    category_id: int = None