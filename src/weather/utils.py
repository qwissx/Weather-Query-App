from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from .models import Weather

def save_query(
    city: str,
    main: str,
    temperature: float,
    latitude: float,
    longitude: float,
    session: AsyncSession,
) -> None:
    weather = Weather(
        city=city,
        main=main,
        temperature=temperature,
        latitude=latitude,
        longitude=longitude
    )
    session.add(weather)

async def get_all_queries(session: AsyncSession) -> list[Weather]:
    result = await session.execute(select(Weather))
    queries = result.scalars().all()
    return queries
