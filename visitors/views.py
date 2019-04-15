from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def info_page(request):
	info_hotel = "this is a 5 Stars Hotel, where you get to come in and relax. Click herre for more details" 
	context = {
	'info_hotel': info_hotel
	}
	
	return render(request, 'info.html', context)


# @login_required
# def make_reservation(request):
# 	pass	
