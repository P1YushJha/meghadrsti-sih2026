from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Profile model for existing user model

# class Profile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     phone = models.IntegerField()

#     def __str__(self):
#         return self.user.username