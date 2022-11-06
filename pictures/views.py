from django.shortcuts import render,redirect
from .models import *
from .forms import *
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def userView(request,pk):
    message=Message.objects.get(id=pk)
    user=Person.objects.get(user=message.created_by)
    print("messsaggge",message)
    #user=message.created_by
    myself=Person.objects.get(user=request.user)
    return render(request,'users.html',{'user':user,'myself':myself})

def category(request):
    if request.user.is_authenticated:
        form=PersonForm()
        if request.method=="POST":
            form=PersonForm(request.POST)
            if form.is_valid():
                cat=form.save(commit=False)
                cat.user=request.user
                cat.save()
            
                return redirect('/')
            else:
                messages.error(request,'An error occured during register')

        return render(request,'category.html',{'form':form})
def loginView(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=="POST":
        username=request.POST.get("username").lower()
        password=request.POST.get("password")

        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, 'NO SUCH USER')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
             messages.error(request, 'username or password is invalid')


    context={}
    return render(request,'login.html',context)

def registerView(request):
    form=UserCreationForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('/')
        else:
            messages.error(request,'An error occured during register')

    return render(request,'register.html',{'form':form})

def logoutView(request):
    logout(request)
    return redirect('/login/')

def home(request):
    if request.user.is_authenticated:
        people=Person.objects.all()
        messages=Message.objects.filter(recieved_by=request.user)
        return render(request,'home.html',{'messages':messages})
    else:
        return redirect('/login')


def searchDonators(request):
    reciever=Person.objects.filter(category='Reciever')
    f=0
    if request.method=='POST':
        a=request.POST.get("a")
        b=request.POST.get("b")
        u=User.objects.get(username=a)
        print('aaaa',a,request.user.username)
        form=Message()
        form.post=b
        form.recieved_by=u
        form.created_by=request.user
        form.save()


    for r in reciever:
        if r.user==request.user:
            f=1

    if f:
        donators=Person.objects.filter(category='Donator')
        return render(request,'search.html',{'donators':donators,'f':f})

    else:
        donators=Person.objects.filter(category='Reciever')
        return render(request,'search.html',{'donators':donators})
