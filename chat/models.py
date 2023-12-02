from django.db import models
from authy.models import User


class Chatroom(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    participants = models.ManyToManyField(User, related_name='chatrooms')
    is_private = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_chatrooms')

    # Add more fields as per your requirements

    def __str__(self):
        return self.name
