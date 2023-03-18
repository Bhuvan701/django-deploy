from django.db import models

# Create your models here.
class images(models.Model):
	name = models.CharField(max_length=30)
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.name

	