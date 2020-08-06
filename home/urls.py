from django.urls import path
<<<<<<< HEAD
=======
from django.conf.urls import url
>>>>>>> 8789d0b3c56097c2ea5a2fd83b7874ddd6590a09
from .import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
]