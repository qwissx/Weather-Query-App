from uuid import UUID, uuid4
from typing import AsyncGenerator
from datetime import datetime

from sqlalchemy import NullPool, DateTime, Uuid
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column

from src.config.settings import st


engine = create_async_engine(st.db_url, poolclass=NullPool)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    time_stamp: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        doc="Время создания записи",
    )
    id: Mapped[UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid4,
        nullable=False,
        index=True,
        doc="UUID созданной записи",
    )


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
