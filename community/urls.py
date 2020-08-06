from django.urls import path
from .views import PostList, PostDelete, PostCreate, PostUpdate, PostDetail

app_name = 'community'

urlpatterns = [
    path("list/",PostList.as_view(), name='list'),
    path("create/",PostCreate.as_view(), name ='create'),
    path("delete/<int:pk>/",PostDelete.as_view(), name = 'delete'),
    path("update/<int:pk>/",PostUpdate.as_view(), name = 'update'),
    path("detail/<int:pk>/",PostDetail.as_view(), name = 'detail'),

]
