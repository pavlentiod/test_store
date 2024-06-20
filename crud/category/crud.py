from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


from db.models import Categorie


async def get_categories(session: AsyncSession):
    stmt = select(Categorie).order_by(Categorie.id)
    result = await session.execute(stmt)
    cats = result.scalars().all()
    return list(cats)


async def get_category_by_name(session: AsyncSession,
                              name: str) -> Categorie | None:
    cat: Categorie = await session.scalar(select(Categorie).where(Categorie.name == name))
    return cat


async def create_category(session: AsyncSession,
                         category: dict) -> Categorie:
    in_db: Categorie = await session.scalar(select(Categorie).where(Categorie.name == category['name']))
    if in_db:
        return in_db
    cat: Categorie = Categorie(**category)
    session.add(cat)
    await session.commit()
    return cat


async def delete_category(
        session: AsyncSession,
        category: Categorie,
) -> None:
    await session.delete(category)
    await session.commit()
