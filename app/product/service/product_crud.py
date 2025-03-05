from app.db.engine import new_session
from app.product.model.product_model import ProductModel
from app.product.schema.product_schem import ProductSchem
from sqlalchemy import select,update
from fastapi import HTTPException,status
class ProductServices:
    @classmethod
    async def add_one(cls,schem:ProductSchem):
        async with new_session() as session:
            model_dict = schem.model_dump()
            model = ProductModel(**model_dict)
            session.add(model)
            await session.commit()
            return {"messege": "Ok"}

    @classmethod
    async def get_all(cls):
        async with new_session() as session:
            model = select(ProductModel).order_by(ProductModel.id)
            result = await session.execute(model)
            products = result.scalars().all()
            if not products:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= "Not found products")
            return products
    
    @classmethod
    async def get_one(cls,id:int):
        async with new_session() as session:
            model = select(ProductModel).filter(ProductModel.id == id)
            result = await session.execute(model)
            product = result.scalars().first()
            if not product:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= "Not found product")
            return product
        
    @classmethod
    async def delete_one(cls,user_id:int):
        async with new_session() as session:
            model = select(ProductModel).filter(ProductModel.id == user_id)
            result = await session.execute(model)
            product = result.scalars().first()
            if not product:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= "Not found product")
            await session.delete(product)
            await session.commit()
            return {"messege":"Ok"}
        
    @classmethod
    async def update_one(cls,schem:ProductModel,user_id:int):
        async with new_session() as session:
            model_dict = schem.model_dump()
            
            model = select(ProductModel).filter(ProductModel.id == user_id)
            result = await session.execute(model)
            product = result.scalars().first()
            
            if not product:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Not found product")
            
            new_product = update(ProductModel).where(ProductModel.id == user_id).values(model_dict)
    
            await session.execute(new_product)
            await session.commit()
            return {"messege":"ok"}
        
    @classmethod
    async def get_all_by_user_id(cls,user_id:int):
        async with new_session() as session:
            model = select(ProductModel).filter(ProductModel.user_id == user_id)
            result = await session.execute(model)
            products = result.scalars().all()
            if not products:
                HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            return products
            
        
    

            