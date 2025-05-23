from ninja import Schema
from datetime import datetime 
from pydantic import EmailStr


class ReminderCreateSchema(Schema):   # Create record in DB (insert a reminder)
    name: str  
    email: EmailStr
    completed: bool
    frequency: str



class ReminderGetSchema(Schema):   # Get record from DB (select a reminder)
    id: int
    name: str                       # Can have multiple output schemas depending on requirement, similar to having specific select queries rather than getting all data
    email: EmailStr
    completed: bool
    frequency: str
    timestamp: datetime



class ReminderListSchema(Schema):    # Get all records from DB (select * from reminder)
    id: int
    name: str                       
    email: EmailStr
    completed: bool
    frequency: str


class MessageSchema(Schema):
    detail: str

