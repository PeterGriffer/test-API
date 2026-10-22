from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    title: str
    director: str
    year: int
    genre: str
    rating: float = 0.0
    description: str = ""

    class Config:
        populate_by_name = True