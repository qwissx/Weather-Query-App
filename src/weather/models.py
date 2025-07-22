from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from src.config.database import Base


class Weather(Base):
    __tablename__ = "weather"

    city: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        doc="Название города в запросе",
    )
    details: Mapped[str] = mapped_column(
        String(100),
        nullable=True,
        doc="Детали запроса",
    )
