from pydantic import BaseModel
from datetime import datetime

class IssueBase(BaseModel):
    title: str
    description: str

class IssueCreate(IssueBase):
    pass


class IssueRead(IssueBase):
    id: str
    user_id: str
    created_at: datetime


    class Config:
        from_attributes = True