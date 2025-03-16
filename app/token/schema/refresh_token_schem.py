from pydantic import BaseModel



class TokenSchem(BaseModel):
    user_id:int
    token:str