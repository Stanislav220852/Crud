from sqlalchemy import select
from app.db.engine import new_session
from app.token.model.refresh_token import RefreshTokenModel
from app.token.schema.refresh_token_schem import TokenSchem

class TokenServices:

    @classmethod
    async def add_one(cls,token:str,id:int):
        async with new_session() as session:
            schem = TokenSchem(token=token,user_id=id)
            model_dict = schem.model_dump()
            
            model = RefreshTokenModel(**model_dict)
            session.add(model)
            await session.commit()

