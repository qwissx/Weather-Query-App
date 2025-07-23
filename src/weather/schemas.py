from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class SWeatherOut(BaseModel):
    id: UUID
    city: str
    time_stamp: datetime
    main: str
    temperature: float
    latitude: float
    longtitude: float

