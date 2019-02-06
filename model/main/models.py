from django.db import models
# Cmreate your models here.
#python3 manage.py sqlmigrate <appame> 0001
class first(models.Model):
	name=models.TextField()
	city=models.CharField(max_length=100,default='DEL')

	def __str__(self):
		return self.name

class age(models.Model):
	#date_of_birth=models.DateField(timezone.now())
	name=models.ForeignKey(first,on_delete=models.CASCADE)

	def __str__(self):
		return self.name