from app.db.base import Base
from sqlalchemy.orm import Mapped


class RefreshTokenModel(Base):
    token:Mapped[str]
    user_id:Mapped[int]