from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from src.config.database import get_db

from .models import Weather

from . import schemas as sch

router = APIRouter(
    prefix="/weather",
    tags=["Weather"],
)
