from django.db import models


# Create your models here.


class Request(models.Model):
      Name = models.CharField(max_length = 20)
      Phone = models.IntegerField()
      Email = models.EmailField(max_length = 30)  
      Special_request = models.CharField(max_length = 280)
      