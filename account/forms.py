from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# 이메일 필드 추가 위해 UserCreationForm 상속해서 추가
class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    # first_name이라는 이미 있는 필드를 별명으로 그냥 사용하면 간편헤서 사용...ㅎㅎ
    first_name = forms.CharField(label="닉네임", max_length=12, min_length=4, required=True, help_text='Required: First Name',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    username = forms.CharField(label="아이디")
    # 별명이 데베에 잘 저장된 것 같지 않음, 아직 미해결...
    class Meta:
        model = User
        fields = ("username",'first_name', "email")

    def __str__(self):
        return self.first_name