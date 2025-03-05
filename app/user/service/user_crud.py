from app.db.engine import new_session
from app.user.model.user_model import UserModel
from app.user.schema.user_schem import UserSchem
from sqlalchemy import select,update
from fastapi import HTTPException,status
from app.core.hash_pass import get_password_hash, verify_password

class UserServices:
    @classmethod
    async def add_one(cls,schem:UserSchem):
        async with new_session() as session:
            model_dict = schem.model_dump()
            model = UserModel(**model_dict)
            model.password = get_password_hash(model.password)
            session.add(model)
            await session.commit()
            return {"messege": "Ok"}

    @classmethod
    async def get_all(cls):
        async with new_session() as session:
            model = select(UserModel).order_by(UserModel.id)
            result = await session.execute(model)
            user = result.scalars().all()
            if not user:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= "Not found user")
            return user
        
    
    @classmethod
    async def get_one(cls,user_id:int):
        async with new_session() as session:
            model = select(UserModel).filter(UserModel.id == user_id)
            result = await session.execute(model)
            user = result.scalars().first()
            if not user:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= "Not found user")
            return user
        
    @classmethod
    async def delete_one(cls,user_id:int):
        async with new_session() as session:
            model = select(UserModel).filter(UserModel.id == user_id)
            result = await session.execute(model)
            user = result.scalars().first()
            if not user:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= "Not found user")
            await session.delete(user)
            await session.commit()
            return {"messege":"Ok"}
        
    @classmethod
    async def update_one(cls,schem:UserSchem,user_id:int):
        async with new_session() as session:
            model_dict = schem.model_dump()
            
            model = select(UserModel).filter(UserModel.id == user_id)
            result = await session.execute(model)
            user = result.scalars().first()
            
            if not user:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Not found user")
            
            new_user = update(UserModel).where(UserModel.id == user_id).values(model_dict)
    
            await session.execute(new_user)
            await session.commit()
            return {"messege":"ok"}
        
    @classmethod 
    async def verify_one(cls,username:str,password:str):
        async with new_session() as session:
            model = select(UserModel).filter(UserModel.username == username and UserModel.password == verify_password(password,UserModel.password))
            result = await session.execute(model)
            user = result.scalars().first()
            if not user:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Not found user")
            return user

            
    
            

            
            
            