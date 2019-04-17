from django.db import models
from django.contrib.auth.models import User


<<<<<<< HEAD

class Room(models.Model):
	ROOM_TYPE = (
		('1p', 'Single Room'),
		('1p_View', 'Single Room with View'),
		('2p', 'Double Room'),
		('2p_View', 'Double Room with View'),
		('Suite' , 'Suite 3Pers'),
		('Suite_ VIP', 'VIP Suite 5Pers'),
	)
	
	room_num = models.IntegerField()
	room_type = models.CharField(max_length= 20, choices=ROOM_TYPE) 
	price = models.FloatField()

	def __str__(self):
		return str(self.room_num)


# class User(models.Model):
# 	first_name= models.CharField(max_length=30)
# 	last_name= models.CharField(max_length=30)
# 	email= models.CharField(max_length=30)
# 	phoneN=  models.IntegerField()

# 	def __str__(self):
# 		return '{} {},'.format(
# 			self.first_name, self.last_name)


class Reservation(models.Model):
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	start_date = models.DateField()
	end_date = models.DateField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return '{} {}'.format(
			self.room.room_num, self.user)
=======
# Create your models here.


class Request(models.Model):
      Name = models.CharField(max_length = 20)
      Phone = models.IntegerField()
      Email = models.EmailField(max_length = 30)  
      Special_request = models.CharField(max_length = 280)
      
>>>>>>> e552b7cbcfb956c419fa63c2189be28189177408
