from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, EmailStr, ConfigDict



class CategoryCreate(BaseModel):
    name: Annotated[str, MinLen(2), MaxLen(30)]
    description: Annotated[str, MinLen(2)]
