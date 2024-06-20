from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import db_helper
from . import crud
from .schemas import CategoryCreate

router = APIRouter()


@router.post("/create", name="Добавление категории")
async def create_category(category: CategoryCreate, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    db_user = await crud.get_category_by_name(session=session, name=category.name)
    if db_user:
        raise HTTPException(status_code=400, detail=f"Категория уже существует")
    prod_dict = await crud.create_category(session, category.model_dump())
    return prod_dict


@router.get('/read/{category_id}', name="Получение информации о категориях")
async def get_category(category_name: str, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    cat = await crud.get_category_by_name(session, name=category_name)
    if cat:
        return cat
    return 'Категории не существует'

@router.get('/read/', name="Все категории")
async def get_categories(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return crud.get_categories(session=session)


