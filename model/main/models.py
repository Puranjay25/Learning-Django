from django.db import models

# Cmreate your models here.
class first(models.Model):
	name=models.TextField()

	def __str__(self):
		return self.name