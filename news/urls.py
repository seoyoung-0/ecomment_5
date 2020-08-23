from django.urls import path

from . import views
from .views import GetIndexView, GetPolicyView, GetIssueView,GetEnterpriseView,GetEtcView

app_name = 'news'

urlpatterns = [
    path('index/',GetIndexView.as_view(), name='index'),
    path('policy/',GetPolicyView.as_view(), name='policy'),
    path('issue/',GetIssueView.as_view(), name='issue'),
    path('enterprise/',GetEnterpriseView.as_view(), name='enterprise'),
    path('etc/',GetEtcView.as_view(), name='etc'),
    
]