from django.contrib import admin
from .models import Tea_Place,Registration,Cart
# Register your models here.


@admin.register((Tea_Place))
class Tea_placeModelAdmin(admin.ModelAdmin):
    list_display=['id','title','selling_price','discounted_price','image','discription']

@admin.register((Registration))
class RegistrationModelAdmin(admin.ModelAdmin):
    list_display=['id','name','lastname','email','contact','gender','taste','state','address','password']

@admin.register((Cart))
class CartModelAdmin(admin.ModelAdmin):
    list_display=['user','tea_place','quantity']