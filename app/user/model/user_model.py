from app.db.base import Base
from sqlalchemy.orm import Mapped,relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.product.model.product_model import ProductModel

class UserModel(Base):
    username:Mapped[str]
    password:Mapped[str]
    email:Mapped[str]
    product: Mapped["ProductModel"] = relationship(back_populates="user")
    role:Mapped[str] = "user"
