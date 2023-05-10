from django.shortcuts import render,redirect
from .models import Tea_Place,Registration,Cart
from django.contrib.auth.hashers import make_password
# Create your views here.

def registration(request):
    return render(request,'registration.html')

def registrationdata(request):
    if request.method=='POST':
        name=request.POST['name']
        lastname=request.POST['lastname']
        email=request.POST['email']
        contact=request.POST['contact']
        gender=request.POST['gender']
        taste=request.POST.getlist('taste')
        state=request.POST['state']
        address=request.POST['address']
        password=make_password(request.POST['password'])
        if Registration.objects.filter(contact=contact).exists():
            return render(request,'registration.html',{'msg':'Contact Number Already Registered'})
        elif Registration.objects.filter(email=email).exists():
            return render(request,'registration.html',{'msg':'Email ID Already Exists'})
        else:
            Registration.objects.create(name=name,lastname=lastname,email=email,contact=contact,gender=gender,taste=taste,state=state,
                                        address=address,password=password)
            return redirect('/')

def login(request):
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')