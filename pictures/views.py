from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    people=Person.objects.all()
    return render(request,'home.html')


def searchDonators(request):
    reciever=Person.objects.filter(category='Reciever')
    f=0
    for r in reciever:
        if r.user==request.user:
            f=1

    if f:
        donators=Person.objects.filter(category='Donator')
        return render(request,'search.html',{'donators':donators,'f':f})

    else:
        donators=Person.objects.filter(category='Reciever')
        return render(request,'search.html',{'donators':donators})
