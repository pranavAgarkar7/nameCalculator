from django.db import models

# Create your models here.
class user_data(models.Model):
	name = models.CharField(max_length=100)
	Ip = models.CharField(max_length=100)
	host_name = models.CharField(max_length=100)
	dateTime1 = models.CharField(max_length=100, default="hi")