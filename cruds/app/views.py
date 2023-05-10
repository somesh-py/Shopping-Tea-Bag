from django.shortcuts import render, redirect
from .models import Tea_Place, Registration, Cart
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.


def registration(request):
    return render(request, 'registration.html')


def registrationdata(request):
    if request.method == 'POST':
        name = request.POST['name']
        lastname = request.POST['lastname']
        email = request.POST['email']
        contact = request.POST['contact']
        gender = request.POST['gender']
        taste = request.POST.getlist('taste')
        state = request.POST['state']
        address = request.POST['address']
        password = make_password(request.POST['password'])
        if Registration.objects.filter(contact=contact).exists():
            return render(request, 'registration.html', {'msg': 'Contact Number Already Registered'})
        elif Registration.objects.filter(email=email).exists():
            return render(request, 'registration.html', {'msg': 'Email ID Already Exists'})
        else:
            Registration.objects.create(name=name, lastname=lastname, email=email, contact=contact, gender=gender, taste=taste, state=state,
                                        address=address, password=password)
            return redirect('/')


def login(request):
    return render(request, 'login.html')


def logindata(request):
    if request.method == 'POST':
        name = request.POST['name']
        contact = request.POST['contact']
        lemail = request.POST['email']
        password = request.POST['password']
        if Registration.objects.filter(contact=contact).exists():
            if Registration.objects.filter(email=lemail).exists():
                data = Registration.objects.get(email=lemail)
                passwordobj = data.password
                if check_password(password, passwordobj):
                    user = Registration.objects.get(email=lemail)
                    # my_dict = {'user': user}
                    # return render(request,'home.html',{'user':user})
                    # return redirect('/home/',permanent=True,**my_dict)
                    data = Tea_Place.objects.all()
                    return render(request, 'home.html', {'data': data,'user':user})
                else:
                    return render(request, 'login.html', {'msg': 'Password Was Incorrect'})
            else:
                return render(request, 'login.html', {'msg': 'Email Was Incorrect'})
        else:
            return render(request, 'login.html', {'msg': 'Contact Was Incorrect'})


def home(request):
    data=Tea_Place.objects.all()
    return render(request,'home.html',{'data':data})

def users(request):
    data=Registration.objects.all()
    return render(request,'users.html',{'data':data})

def addtocart(request,id,uid):
    user=Registration.objects.get(id=uid)
    data=Tea_Place.objects.get(id=id)
    return render(request,'addtocart.html',{'data':data,'user':user})

def intocart(request):
    if request.method=='POST':
        product_id=request.POST.get('prod_id')
        user_id=request.POST.get('user_id')
        print('aa',product_id)
        print('aa',user_id)
        user=Registration.objects.get(id=user_id)
        item=Tea_Place.objects.get(id=product_id)
        cart=Cart.objects.create(user=user,tea_place=item).save()
        return redirect('/home/')