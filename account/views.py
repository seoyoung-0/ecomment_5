from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from account.forms import UserForm
from django.contrib import messages
from django.views.generic.base import View
from django.views.generic.list import ListView
from community.models import Post


def signup(request):

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = request.POST["first_name"]
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            # 신규 사용자 저장 후 자동 로그인
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home:home')
    else:
        form = UserForm()

    return render(request, 'account/signup.html', {'form': form})

def checkbox(request):
    return render(request,"account/checkbox.html")

class mypage(View):
    def get(self, request):
        posts = Post.objects.all()
        my_posts_list = posts.filter(author = request.user)
        my_posts_list=my_posts_list[:2]
        return render(request, 'account/mypage.html', {'my_posts_list':my_posts_list})

