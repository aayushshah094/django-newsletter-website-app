from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank = True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    profile_pic = models.ImageField(default="default.jpg", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
	    return self.name

