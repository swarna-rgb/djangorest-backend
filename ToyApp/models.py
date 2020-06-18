from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# many toys -> one user
# If i delete toy, user is not deleted
# If i pull the user, all of that user's toys should be displayed

# class ToyStoreAPIUser(AbstractUser):
#     is_manager = models.BooleanField(null=True, blank=True)
#     is_employee = models.BooleanField(null=True, blank=True)
#     def __str__(self):
#         return self.username

# class Manager(models.Model):
#     user = models.OneToOneField(ToyStoreAPIUser,related_name='related_mtoys', on_delete=models.CASCADE)
#     fname = models.CharField(max_length=30)
#     lname = models.CharField(max_length=30)
#     def __str__(self):
#         return self.username
#
# class Employee(models.Model):
#     user = models.OneToOneField(ToyStoreAPIUser,related_name='related_etoys', on_delete=models.CASCADE)
#     fname = models.CharField(max_length=30)
#     lname = models.CharField(max_length=30)
#     def __str__(self):
#         return self.username

class Toy(models.Model):
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)