from django.shortcuts import render
from visitors import forms
from visitors import models
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Reservation




def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

<<<<<<< HEAD

def info_page(request):
	info_hotel = "this is a 5 Stars Hotel, where you get to come in and relax. Click herre for more details" 
	context = {
	'info_hotel': info_hotel,
	}
	
	return render(request, 'info.html', context)



# @login_required
# def make_reservation(request):
# 	pass	



def booking(request):
	free_room = Reservation.objects.all()

	context= {

	}
	return render(request, 'booking.html', context)

# @login_required
# def make_reservation(request):
# 	pass	

 
def Request_page(request):

    form = forms
    data = models.Contact.objects.all()

    if(request.method=='POST'):

        Name = request.POST['Name']
        Phone = request.POST['Phone']
        Email = request.POST['Email']
        Special_request = request.POST['Special_request']
       
        add = models.Contact(Name=Name, Phone=Phone, Email=Email, Special_request=Special_request)      
        add.save()
 
    return render(request,'request.html',locals())

