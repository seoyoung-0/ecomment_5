from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView,CreateView, DeleteView
from django.views.generic.detail import DetailView
from .models import *

class PostList(ListView):
    model = Post
    template_name_suffix = '_list'

class PostCreate(CreateView):
    model = Post
    fields = ['title','category','text','image']
    template_name_suffix = '_create'
    success_url ='/'

class PostUpdate(UpdateView):
    model = Post
    fields = ['title','category','text','image']
    template_name_suffix = '_update'
    success_url ='/'

class PostDelete(DeleteView):
    model = Post
    template_name_suffix = '_delete'
    success_url ='/'

class PostDetail(DetailView):
    model = Post
    template_name_suffix = '_detail'
