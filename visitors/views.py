from django.shortcuts import render 

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def info_page(request):
	info_hotel = "this is a 5 Stars Hotel, where you get to come in and relax. Click herre for more details" 
	context = {
	'info_hotel': info_hotel
	}
	
	return render(request, 'info.html', context)
	
