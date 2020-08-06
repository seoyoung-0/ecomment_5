from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering =['name']


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    title = models.CharField(max_length = 200 )
    category = models.ForeignKey(Category, on_delete = models.SET_NULL,null=True, blank=True)
    text = models.TextField()
    image = models.ImageField(upload_to= 'community/community_photo/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # like = models.ManyToManyField(User, related_name='list_post', blank=True)
    # unlike = models.ManyToManyField(User, related_name='list_post', blank=True)
    # favorite = models.ManyToManyField(User, related_name='favorite_post', blank=True)
    # # views = models.IntegerField

    def __str__(self):
        return "text:"+self.text
        # 입력받은 객체의 문자열 버전을 반환하는 함수 
        # 내장 str 클래스 의 생성자 메소드를 실행, 인자로 객체 전달 하는 것 

    class Meta:
        ordering = ['-created']
        # 모델의 정렬 순서 지정 : 여러개 지정 시 필드 이름을 리스트로 나열 
        # - 붙으면 내림차순, 기본은 오름차순 