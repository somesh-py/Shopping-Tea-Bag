from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tea_Place(models.Model):
    title=models.CharField(max_length=50)
    selling_price=models.CharField(max_length=50)
    discounted_price=models.CharField(max_length=50)
    image=models.ImageField(upload_to="images")
    discription=models.TextField()

STATE_CHOISES=(
    ('mp','mp'),
    ('rajasthan','rajasthan'),
    ('gujrat','gujrat'),
    ('maharashtra','maharashtra'),
    ('odissa','odissa'),
    ('telangana','telangana')
)

GENDER=(
    ('male','male'),
    ('female','female')
)

TASTE=(
    ('sweet','sweet'),
    ('sour','sour'),
    ('salty','salty'),
    ('bitter','bitter'),
    ('savory','savory')
)

class Registration(models.Model):
    name=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    contact=models.IntegerField()
    gender=models.CharField(choices=GENDER,max_length=50)
    taste=models.CharField(choices=TASTE,max_length=50)
    state=models.CharField(choices=STATE_CHOISES,max_length=50)
    address=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class Cart(models.Model):
    user=models.ForeignKey(Registration,on_delete=models.CASCADE)
    tea_place=models.ForeignKey(Tea_Place,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)