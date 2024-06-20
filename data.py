import asyncio
import random

import crud.category.crud
import crud.product.crud
from db.models import db_helper

products = [
    {"name": f"category {i % 20}; name {i}", "description": f"description {i}", "price": random.randint(0, 10000),
     "weight": random.randint(0, 10000), "category_id": i % 20 + 1} for i in range(100)
]

categories = [
    {"name": f"{i % 20}", "description": f"description for category {i % 20}"} for i in range(100)
]


async def add_data():
    async with db_helper.session_factory() as session:
        for category in categories:
            await crud.category.crud.create_category(session, category=category)
        for product in products:
            await crud.product.crud.create_product(session, product=product)

