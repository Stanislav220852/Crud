from fastapi import APIRouter
from app.user.service.user_crud import UserServices
from app.user.schema.user_schem import UserSchem

user_router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@user_router.get("/")
async def get_all():
    return await UserServices.get_all()

@user_router.get("/{user_id}")
async def get_one(id:int):
    return await UserServices.get_one(user_id=id)

@user_router.post("/")
async def add_one(schem:UserSchem):
    return await UserServices.add_one(schem=schem)

@user_router.delete("/{user_id}")
async def delete_one(id:int):
    return await UserServices.delete_one(user_id=id)

@user_router.put("/{user_id}")
async def update_one(id:int,schem:UserSchem):
    return await UserServices.update_one(user_id=id,schem=schem)
