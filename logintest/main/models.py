from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
	mobile = models.CharField(max_length=50,null=True)

	def __str__(self):
		return self.email