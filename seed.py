import os
import random
import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotelproject.settings')

django.setup()

from django.contrib.auth.models import User
from visitors.models import *


f = Faker()

def fake_first_n():
	return f.first_name()

def fake_last_n():
	return f.last_name()

def fake_email():
	return f.email()

def fake_password():
	password_hard_coded = 123456789
	# return fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
	return password_hard_coded


def create_user(num):
	for i in range(0, num):
		first_n = fake_first_n()
		last_n = fake_last_n()
		email = fake_email()
		user = User.objects.create_user(username=email, password=fake_password(),first_name=first_n, last_name=last_n)
		user.save()

# create_user(10)

# def fake_room_num():
# 	pass

# def create_room(num):
	

# def fake_start_date():
# 	return fake.past_date(start_date="-30d", tzinfo=None)

# def fake_end_date():
# 	return fake.past_date(start_date="-5d", tzinfo=None)


# vehicles = Vehicle.objects.all()
# 	return random.choice(vehicles)
# def create_reservation(num):
# 	for i in range(0, num):
# 		start_date = fake_start_date()
# 		end_date = fake_end_date()
# 		room_num = 
# 		pass