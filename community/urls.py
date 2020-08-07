from django.urls import path
from .views import PostList, PostDelete, PostCreate, PostUpdate, PostDetail

app_name = 'community'

urlpatterns = [
    path("", PostList.as_view(), name="index"),
    path("list/",PostList.as_view(), name='list'),
    path("create/",PostCreate.as_view(), name ='create'),
    path("delete/<int:pk>/",PostDelete.as_view(), name = 'delete'),
    path("update/<int:pk>/",PostUpdate.as_view(), name = 'update'),
    path("detail/<int:pk>/",PostDetail.as_view(), name = 'detail'),

]

# 이미지 url 확실히 설정해서 사진 오류 없앰
from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)