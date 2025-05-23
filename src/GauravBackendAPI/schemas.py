from ninja import Schema
from pydantic import EmailStr

class UserSchema(Schema):
    username: str
    is_authenticated: bool 


class UserSignupSchema(Schema):
    username: str
    email: EmailStr
    password: str