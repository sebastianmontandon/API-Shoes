from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username: str
    email: Optional[str]
    full_name: Optional[str]
    disabled: Optional[bool]
    hashed_password: str