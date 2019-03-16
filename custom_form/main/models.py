from django.db import models
# Create your models here.
class user(models.Model):
	first_name=models.TextField()
	last_name=models.TextField()
	username=models.TextField()
	email=models.TextField()
	password=models.TextField()
	confirm_password=models.TextField()

	def __str__(self):
		return self.first_name