from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView,CreateView, DeleteView
from django.views.generic.detail import DetailView
from .models import *

from django.core.paginator import Paginator

class PostList(ListView):
    model = Post
    template_name_suffix = '_list'
    context_object_name = 'Posts'
    paginate_by = 8
    #몇 개씩 나올지 수정하기 

class PostCreate(CreateView):
    model = Post
    fields = ['title','category','text','image']
    template_name_suffix = '_create'
    success_url ='/community/list'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            # 올바르다면
            form.instance.save()
            return redirect('/community/list')
        else:
            # 올바르지 않다면
            return self.render_to_response({'form': form})

class PostUpdate(UpdateView):
    model = Post
    fields = ['title','category','text','image']
    template_name_suffix = '_update'
    success_url ='/community/list'

class PostDelete(DeleteView):
    model = Post
    template_name_suffix = '_delete'
    success_url ='/'

class PostDetail(DetailView):
    model = Post
    template_name_suffix = '_detail'

