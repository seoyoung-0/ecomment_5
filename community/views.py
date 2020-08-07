from django.shortcuts import redirect, render
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

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            # 올바르다면
            form.instance.save()
            return redirect('/')
        else:
            # 올바르지 않다면
            return self.render_to_response({'form': form})

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

