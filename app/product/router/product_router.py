from fastapi import APIRouter
from app.product.service.product_crud import ProductServices
from app.product.schema.product_schem import ProductSchem 

product_router = APIRouter(
    prefix="/product",
    tags=["product"]
)

@product_router.get("/")
async def get_all():
    return await ProductServices.get_all()

@product_router.get("/{product_id}")
async def get_one(id:int):
    return await ProductServices.get_one(user_id=id)

@product_router.post("/")
async def add_one(schem:ProductSchem):
    return await ProductServices.add_one(schem=schem)

@product_router.delete("/{product_id}")
async def delete_one(id:int):
    return await ProductServices.delete_one(user_id=id)

@product_router.put("/{product_id}")
async def update_one(id:int,schem:ProductSchem):
    return await ProductServices.update_one(user_id=id,schem=schem)

@product_router.get("/user/{user_id}")
async def get_all_by_user_id(user_id:int):
    return  await ProductServices.get_all_by_user_id(user_id=user_id)

