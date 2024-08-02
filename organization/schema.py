from typing import List
from pydantic import BaseModel, Field
from bson import ObjectId
from datetime import datetime


class Organization(BaseModel):
    name: str
    token: str = None
    remaining: float = None

class Device(BaseModel):
    oraganization: ObjectId
    device_token: str = None
    active: bool = True

class Employ(BaseModel):
    organization: ObjectId
    name: str
    employ_id: int
    images: List[str]
    done: bool = False

class Payment(BaseModel):
    organization: ObjectId
    price: int
    created_at: datetime = Field(default_factory=datetime.utcnow)
