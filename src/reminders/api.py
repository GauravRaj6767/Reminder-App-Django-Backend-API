from ninja import Router
from typing import List
from .schemas import ReminderListSchema, ReminderGetSchema, ReminderCreateSchema, MessageSchema
from .models import Reminders  
from django.shortcuts import get_object_or_404
from ninja_jwt.authentication import JWTAuth



router = Router()
#Get all reminders
@router.get("", response=List[ReminderListSchema], auth=JWTAuth())
def list_reminder_entries(request):
    qs =  Reminders.objects.filter(user=request.user)
    return qs

#Create new reminder 
@router.post("", response=ReminderGetSchema,  auth=JWTAuth())
def create_reminder_entry(request, data:ReminderCreateSchema):
    obj = Reminders(**data.dict())
    obj.user = request.user
    obj.save()
    return obj   

#Gets individual reminder based on entry_id
@router.get("{entry_id}/", response=ReminderGetSchema, auth=JWTAuth())
def get_reminder_entry(request,entry_id: int):
    obj =  get_object_or_404(Reminders, id=entry_id, user=request.user)
    return obj


# PUT route for updating 'completed' status or updating all fields in reminder in edit form
@router.put("{entry_id}/", auth=JWTAuth(), response=ReminderGetSchema)
def update_reminder_entry(request, entry_id: int, data: ReminderCreateSchema):
    reminder = get_object_or_404(Reminders, id=entry_id, user=request.user)
    for field, val in data.dict().items():  #  exclude_none=True only updates the fields that were actually sent
        setattr(reminder, field, val)
    reminder.save()
    return reminder


# DELETE method to delete specific record from DB
@router.delete("{entry_id}/delete/", auth=JWTAuth(), response=MessageSchema)
def delete_reminder_entry(request, entry_id: int):
    reminder = get_object_or_404(Reminders, id=entry_id, user=request.user)
    reminder.delete()
    return { "detail": "Reminder deleted successfully." }



