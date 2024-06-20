from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import db_helper, Product
from . import crud
from .schemas import ProductCreate, ProductUpdate

router = APIRouter()


@router.post("/create", name="Добавление продуктов")
async def create_product(product: ProductCreate, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    db_user = await crud.get_product_by_name(session=session, name=product.name)
    if db_user:
        raise HTTPException(status_code=400, detail=f"Продукт уже существует")
    prod_dict = await crud.create_product(session, product.model_dump())
    return prod_dict


@router.get('/read/{product_id}', name="Чтение существующих продуктов")
async def get_product(product_id: int, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    product: Product | None = await crud.get_product(session, product_id=product_id)
    if product:
        return product
    return 'Product isn\'t exist'



@router.patch("/update/{product_id}", name="Обновление существующих продуктов")
async def update_product(
        product_update: ProductUpdate,
        product_id: int,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    prod = await crud.get_product(session=session, product_id=product_id)
    if prod:
        return await crud.update_product(
            session=session,
            product=prod,
            update=product_update.model_dump()
        )


@router.delete("/delete/{product_id}", status_code=status.HTTP_204_NO_CONTENT, name="Удаление существующих продуктов")
async def delete_product(
        product_id : int,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    prod = await crud.get_product(session=session, product_id=product_id)
    if prod:
        await crud.delete_product(session=session, product=prod)


