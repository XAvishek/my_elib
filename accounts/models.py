from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    """
    User profile model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_no = models.IntegerField(null=True, blank=True)
