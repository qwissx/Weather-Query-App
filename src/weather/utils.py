import httpx

from src.config.settings import st


async def fetch_city_weather(
    city_name: str,
    state_code: str | None = None,
    country_code: int | None = None,
    limit: int = 5
) -> dict:
    base_url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": f"{city_name},{state_code or ''},{country_code or ''}".strip(','),
        "limit": limit,
        "appid": st.weather_api_key,
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(base_url, params=params)
        response.raise_for_status()  # Проверка на ошибки HTTP
        return response.json()
