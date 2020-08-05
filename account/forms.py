from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# 이메일 필드 추가 위해 UserCreationForm 상속해서 추가
class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    nickname = forms.CharField(label="별명")
    # 별명이 데베에 잘 저장된 것 같지 않음, 아직 미해결...
    class Meta:
        model = User
        fields = ("username", "email", "nickname")

    def __str__(self):
        return self.username