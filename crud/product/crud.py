from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from crud.product.schemas import ProductUpdate
from db.models import Product


async def get_product(session: AsyncSession,
                      product_id: int) -> Product | None:
    product = await session.get(Product, product_id)
    return product


async def get_product_by_name(session: AsyncSession,
                              name: str) -> Product | None:
    product: Product = await session.scalar(select(Product).where(Product.name == name))
    return product


async def create_product(session: AsyncSession,
                         product: dict) -> Product:
    in_db: Product = await session.scalar(select(Product).where(Product.name == product['name']))
    if in_db:
        return in_db
    prod: Product = Product(**product)
    print(prod)
    session.add(prod)
    await session.commit()
    return prod


async def update_product(
        session: AsyncSession,
        product: ProductUpdate,
        update: dict
) -> Product:
    for name, value in update.items():
        if value:
            setattr(product, name, value)
    await session.commit()
    return product


async def delete_product(
        session: AsyncSession,
        product: Product,
) -> None:
    await session.delete(product)
    await session.commit()
