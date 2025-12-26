from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    email: str
    name: Optional[str] = None

class UserCreate(UserBase):
    firebase_uid: str

class UserRead(UserBase):
    id: str
    firebase_uid: str
    created_at: datetime

    class Config:
        from_attributes = True