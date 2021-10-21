from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=150)
#     email = models.EmailField(max_length=200, unique=True)
#     password = models.CharField(max_length=200)
#
#     objects =  UserManager()
#
#     def __str__(self):
#         return self.username


class Profile(models.Model):
    account_type = models.CharField(max_length=100)
    mobile_number = models.IntegerField(unique=True)
    country_of_residence = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.account_type
