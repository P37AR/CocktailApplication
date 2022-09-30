from django.db import models
from django.contrib.auth.models import User as DjangoUser


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE, related_name='app_user')

    def __str__(self):
        return self.name + " " + self.surname
