from django.urls import path

from . import views
from .views import GetPolicyView

app_name = 'news'

urlpatterns = [
    path('policy/',GetPolicyView.as_view(), name='policy'),
    
]