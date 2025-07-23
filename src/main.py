from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles

from src.weather.router import router as wz_router

app = FastAPI(base_url="/api", docs_url=None)

app.mount("/static", StaticFiles(directory="src/static"), name="static")

app.include_router(wz_router)

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url=f"https://unpkg.com/swagger-ui-dist@5.18.2/swagger-ui-bundle.js",
        swagger_css_url=f"https://unpkg.com/swagger-ui-dist@5.18.2/swagger-ui.css",
    )
