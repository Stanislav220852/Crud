from pydantic import BaseModel,field_validator
from typing import Annotated
from annotated_types import MaxLen,MinLen


class ProductSchem(BaseModel):
    name:Annotated[str,MaxLen(30),MinLen(3)]
    price:int
    user_id:int

   
class ProductBase(ProductSchem):
    id:int