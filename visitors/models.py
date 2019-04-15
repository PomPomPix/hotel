from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# TYPE_CHOICES = (
# 	(1, _('Single Room witout View')),
# 	(2, _('Double Room without View')),
# 	(3, _('Single Room with View')),
# 	(4, _('Double Room with View')),
# 	(5, _('Suite')),
# 	(6, _('Studio')),
# )

class Room(models.Model):
	number = models.IntegerField()
	# room_type = models.IntegerField(choices=TYPE_CHOICES) 
	price = models.FloatField()

	# user = models.ForeignKey(User, on_delete=models.CASCADE)
	# review = models.ForeignKey(MovieReview, on_delete=models.CASCADE)
	# content = models.TextField()
	# pub_date = models.DateTimeField(default=timezone.now)


# class Guest(models.Model):
#   guest = request.user
#   # first_name =  
#   # last_name = 
#   # email = 
#   pass


class Reservation(models.Model):
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	room_num = models.ForeignKey(Room, on_delete=models.CASCADE)
	guest = models.ForeignKey(User, on_delete=models.CASCADE)
