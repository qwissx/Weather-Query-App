from pathlib import Path

from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession

from src.config.database import get_db

from .services import WeatherService

from . import schemas as sch


templates = Jinja2Templates(directory="src/templates")

router = APIRouter(
    prefix="/weather",
    tags=["Weather"],
)


@router.get(
    path="/test",
    description="Эндпоинт для получения html формы")
async def get_weather_page():
    html_weather = Path("src/templates/weather.html")
    return HTMLResponse(
        content=html_weather.read_text(),
        status_code=200,
    )


@router.get(
    path="/",
    description="Эндпоинт для получения истории",
)
async def get_weather_history(
    request: Request,
    session: AsyncSession = Depends(get_db),
    weather_client: WeatherService = Depends(WeatherService.get_client),
):
    history = await weather_client.get_history(session)
    return templates.TemplateResponse(
        "history.html",
        {"request": request, "history": history}
    )


@router.get(
    path="/{city}",
    description="Эндпоинт для получения погоды", 
)
async def get_city_weather(
    city: str,
    session: AsyncSession = Depends(get_db),
    weather_client: WeatherService = Depends(WeatherService.get_client),
):
    description = await weather_client.get_weather(city, session)
    await session.commit()
    return description

