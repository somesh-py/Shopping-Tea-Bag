from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('registration/',views.registration),
    path('regdata/',views.registrationdata),
    path('',views.login),
    path('logdata/',views.logindata),
    path('home/',views.home),
    path('users/',views.users),
    path('addtocart/',views.addtocart),
    path('intocart/',views.intocart),
    path('addtocart/<int:id>/<int:uid>',views.addtocart,name="addtocart"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
