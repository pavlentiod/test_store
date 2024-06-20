from fastapi import APIRouter


from .product.views import router as product_router
from .category.views import router as category_router
from .sorting.views import router as sorting_router

router = APIRouter()

router.include_router(product_router, prefix='/product', tags=['Продукты'])
router.include_router(category_router, prefix='/category', tags=['Категории'])
router.include_router(sorting_router, prefix='/sort', tags=['Сортировка продуктов'])