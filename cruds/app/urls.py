from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('registration',views.registration),
    path('regdata/',views.registrationdata),
    path('',views.login),
    path('home',views.home),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
