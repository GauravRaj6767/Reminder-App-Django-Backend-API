from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Reminders(models.Model):
    user = models.ForeignKey(User, default=None, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.TextField()
    email = models.EmailField()
    completed = models.BooleanField(default=False) 
    frequency = models.TextField()   # Daily, Weekly, Monthly
    timestamp = models.DateTimeField(auto_now_add=True)


# And when working with a model, use the Meta class to tell Django the name of the database table to use for the model.

# class Fruit(AbstractModel):

#     name = models.CharField(max_length=100)

#     class Meta:
#         db_table = '"coreschema". "fruit"'
    
    