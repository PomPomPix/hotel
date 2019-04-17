from django.contrib import admin
from .models import Room, Reservation 
from .models import Request

admin.site.register(Room)
admin.site.register(Reservation)


# Register your models here.

admin.site.register(Request)
