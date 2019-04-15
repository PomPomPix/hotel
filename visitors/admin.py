from django.contrib import admin
from .models import User, Rooms, Reservation, Suplier

admin.site.register(Rooms)
admin.site.register(Reservation)
admin.site.register(User)
admin.site.register(Suplier)
