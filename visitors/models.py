from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Rooms(models.Model):
	ROOM_TYPE = (
		('1p', 'Single Room'),
		('1p_View', 'Single Room with View'),
		('2p', 'Single Room with View'),
		('2p_View', 'Double Room with View'),
		('Suite' , 'Suite 3Pers'),
		('Suite_ VIP', 'VIP Suite 5Pers'),
	)
	
	room_num = models.IntegerField()
	room_type = models.IntegerField(choices=ROOM_TYPE) 
	price = models.FloatField()

	def __str__(self):
		return self.room_num


class User(models.Model):
	first_name= models.CharField(max_length=30)
	last_name= models.CharField(max_length=30)
	email= models.CharField(max_length=30)
	phoneN=  models.IntegerField()

	def __str__(self):
		return '{} {},'.format(
			self.first_name, self.last_name)


class Reservation(models.Model):
	room_num = models.ForeignKey(Rooms, on_delete=models.CASCADE)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.room_num





class Suplier(models.Model):
	first_name= models.CharField(max_length=30)
	last_name= models.CharField(max_length=30)
	email= models.CharField(max_length=30)
	phoneN=  models.IntegerField()

	def __str__(self):
		return '{} {},'.format(
			self.first_name, self.last_name)
