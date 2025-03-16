from pydantic import BaseModel, ConfigDict,EmailStr
from typing import Annotated
from annotated_types import MaxLen,MinLen


class UserSchem(BaseModel):
    username:Annotated[str,MinLen(3),MaxLen(30)]
    password:Annotated[str,MaxLen(8),MinLen(4)]
    email:EmailStr
    

class UserBase(UserSchem):
    id:int
    role:str
    
