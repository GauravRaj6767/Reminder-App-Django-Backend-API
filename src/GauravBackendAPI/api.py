from __future__ import annotations

from ninja import NinjaAPI, Schema
from ninja_extra import NinjaExtraAPI
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.controller import NinjaJWTDefaultController
from .schemas import UserSchema, UserSignupSchema


from django.contrib.auth.models import User  # User table 
from django.db import IntegrityError



api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)
api.add_router("/reminders/", "reminders.api.router")


@api.get("/hello/")
def testFunc(request):
    # print("HELLO")
    print(request)
    return {"message": "HELLO TESTING----"}


@api.get("/me/", response=UserSchema)
def me(request):
    # print("GET ME")
    print(request)
    return request.user


@api.post("/signup/", response={201: UserSchema, 400: dict})
def signup(request, data : UserSignupSchema):
    try:
        # print("CHECK -- > " + data)
        user = User.objects.create_user(
        username=data.username,
        email=data.email,
        password=data.password,
        )
        return 201, user   
    except IntegrityError:
        return {"error": "Username or email already exists"}

