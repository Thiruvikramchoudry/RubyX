from django.db import models
from datetime import datetime

# Create your models here.

class bot_messages(models.Model):
    username=models.CharField(max_length=100)
    message_type=models.CharField(max_length=10)
    message=models.TextField(max_length=1000)
    date_time=models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.username