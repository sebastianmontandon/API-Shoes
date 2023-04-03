from pydantic import BaseModel
from typing import Optional

class Shoes(BaseModel):
    id: Optional[str]
    sku: str
    name: str
    description: Optional[str]
    size: list[str]
    availability: bool
    price: int
    reviews: Optional[str]
    images: Optional[list[str]]