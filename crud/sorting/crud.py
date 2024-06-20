from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import Product


async def sort_products(session: AsyncSession, filter: int):
    if filter == 1:
        stmt = select(Product).order_by(Product.price)
    elif filter == 2:
        stmt = select(Product).order_by(Product.weight)
    elif filter == 3:
        stmt = select(Product).order_by(Product.name)
    elif filter == 4:
        stmt = select(Product).order_by(Product.category_id)
    else:
        stmt = select(Product).order_by(Product.id)
    result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)

