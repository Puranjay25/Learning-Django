from django.db import models

# Create your models here.
class user(models.Model):
	name=models.TextField()
	username=models.CharField(max_length=15)
	password=models.TextField()
	confirm_pass=models.TextField()

	def __int__(self):
		return self.username