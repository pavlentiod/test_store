from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import db_helper, Product
from . import crud


router = APIRouter()


@router.get("/", name="Сортировка продуктов", description="Параметры сортировки:\n1. Цена\n2. Вес\n3. Название\n4. Категория\n\nНеобходимое значение требуется ввести как параметр filter")
async def create_product(filter: int, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.sort_products(filter=filter, session=session)