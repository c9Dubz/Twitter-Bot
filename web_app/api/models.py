from django.db import models
import string
import random

def gen_unique_user_id():
    length = 8
    
    while True:
        user_id = ''.join(random.choices(string.ascii_uppercase, k=length))
        if User.objects.filter(user_id=user_id).count() == 0:
            break
        
    return user_id

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=8, default="00000000", unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    