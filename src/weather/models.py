from sqlalchemy import String, Float
from sqlalchemy.orm import mapped_column, Mapped

from src.config.database import Base


class Weather(Base):
    __tablename__ = "weather"

    city: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        doc="Название города в запросе",
    )
    main: Mapped[str] = mapped_column(
        String(100),
        nullable=True,
        doc="Описание текущего состояния",
    )
    temperature: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        doc="Температура в Цельсии",
    )
    latitude: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        doc="Географическая ширина",
    )
    longitude: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        doc="Географическая долгота",
    )
