from core.model import *
from authy.models import User


class Chatroom(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    participants = models.ManyToManyField(User, related_name='chatrooms')
    is_private = models.BooleanField(default=False)
    max_participants = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_chatrooms')

    # Add more fields as per your requirements

    def __str__(self):
        return self.name


class Message(BaseModel):
    content = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_chatrooms')
    chat_room = models.ForeignKey(Chatroom, on_delete=models.CASCADE, related_name='messages')

    class Meta:
        ordering = ['-created_at']  # Ordering messages by creation timestamp

    def __str__(self):
        return f"Message from {self.user.username} at {self.created_at}"
