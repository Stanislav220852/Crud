from app.db.base import Base
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey,Integer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.user.model.user_model import UserModel


class ProductModel(Base):
    name:Mapped[str]
    price:Mapped[int]
    user_id = mapped_column(
        Integer,
        ForeignKey("usermodels.id"),
        nullable=False,
    )

    user: Mapped[list["UserModel"]] = relationship(back_populates="product")