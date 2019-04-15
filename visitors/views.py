from django.shortcuts import render
from visitors import forms
from visitors import models
from django.http import HttpResponse



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

 
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