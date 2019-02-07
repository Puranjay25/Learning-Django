from django.db import models

# Create your models here.
class details(models.Model):
	name=models.TextField()
	city=models.TextField()

	def __str__(self):
		return self.name