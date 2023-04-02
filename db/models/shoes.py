from pydantic import BaseModel
from typing import Optional

class Shoes(BaseModel):
    id: Optional[str]
    name: str
    description: str
    size: str
    availability: bool
    price: int
    reviews: str
    images: list[str]