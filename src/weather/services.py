import httpx
from sqlalchemy.ext.asyncio import AsyncSession

from src.config.settings import st

from . import utils as utl


class WeatherAPI:
    @staticmethod
    async def fetch_city_cords(
        city_name: str,
        state_code: str | None = None,
        country_code: int | None = None,
        limit: int = 1,
    ) -> dict:
        base_url = "http://api.openweathermap.org/geo/1.0/direct"
        params = {
            "q": f"{city_name},{state_code or ''},{country_code or ''}".strip(','),
            "limit": limit,
            "appid": st.weather_api_key,
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(base_url, params=params)
            response.raise_for_status() 
            data = response.json()
            return {
                "lat": float(data[0]["lat"]),
                "lon": float(data[0]["lon"]),
            }

    @staticmethod
    async def fetch_city_weather(latitude: float, longitude: float) -> dict:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "lat": latitude,
            "lon": longitude,
            "appid": st.weather_api_key,
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status() 
            data = response.json()
            temp = round(float(data["main"]["temp"]) - 273.15, 2)
            return {
                "main": data["weather"][0]["main"],
                "tempreture": temp,
            }


class WeatherService:
    @classmethod
    async def get_client(cls):
        return WeatherService()

    @staticmethod
    async def get_weather(city_name: str, session: AsyncSession) -> dict:
        cords = await WeatherAPI.fetch_city_cords(city_name)
        weather = await WeatherAPI.fetch_city_weather(cords["lat"], cords["lon"])
        utl.save_query(
            city_name,
            weather["main"],
            weather["tempreture"],
            cords["lat"],
            cords["lon"],
            session,
        )
        return weather

    @staticmethod
    async def get_history(session: AsyncSession) -> dict:
        return await utl.get_all_queries(session)

