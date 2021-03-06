from django.db.models import Q
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView,CreateView, DeleteView
from django.views.generic.detail import DetailView
from .models import *
from django.views.generic.base import View
from urllib.parse import urlparse
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib import messages

from django.core.paginator import Paginator
from .forms import PostForm, CommentForm


# class mypage(View):
#     def get(self, request):
#         posts = Post.objects.all()
#         my_posts_list = posts.filter(author = request.user)
#         my_posts_list=my_posts_list[:2]
#         return render(request, 'account/mypage.html', {'my_posts_list':my_posts_list})
class PostMain(View):
    model = Post
    template_name='community/post_main.html'
    cats = Category.objects.all()

    def get(self, request):

        newer_list = Post.objects.all().order_by('-created')
        newer_list=newer_list[:3]

        like_list = Post.objects.all().order_by('-like')
        like_list = like_list[:4]

        watch_list = Post.objects.all().order_by('-hits')
        watch_list = watch_list[:4]
  
        return render(request, 'community/post_main.html', {'like_list':like_list,'watch_list':watch_list, 'newer_list':newer_list})

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostMain,self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class PostList(ListView):
    model = Post
    template_name_suffix = '_list'
    context_object_name = 'Posts'
    paginate_by = 8
    #몇 개씩 나올지 수정하기 
    cats = Category.objects.all()

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostList,self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryView(request,cats):
    category_posts = Post.objects.filter(category=cats)
    cat_menu = Category.objects.all()
    return render(request, 'community/categories.html',{'cats':cats,'category_posts':category_posts,'cat_menu':cat_menu})

class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name ='community/post_create.html'
    success_url ='/community/'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            # 올바르다면
            form.instance.save()
           # messages.add_message(self.request, messages.INFO, '새 글이 등록되었습니다.')  # 첫번째, 초기지원
           #  messages.info(self.request, '새 글이 등록되었습니다.')  # 두번째, shortcut 형태
            return redirect('/community/list')
        else:
            # 올바르지 않다면
            messages.error(self.request, 'Error!')
            return self.render_to_response({'form': form})

class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name_suffix = '_update'
    success_url ='/community/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            messages.warning(request,'수정 권한이 없습니다.')
            return HttpResponseRedirect('/community/list')
        else:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)

# class PostDelete(DeleteView):
#     model = Post
#     template_name_suffix = '_delete'
#     success_url ='/community/list'
#
#     def dispatch(self, request, *args, **kwargs):
#         object = self.get_object()
#         if object.author != request.user:
#             messages.warning(request, '삭제 권한이 없습니다. ')
#             return HttpResponseRedirect('/community/list')
#         else:
#             return super(PostDelete, self).dispatch(request, *args, **kwargs)
def post_delete(request, post_id):

    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('community:detail', post_id=post.post_id)
    else:
        post.delete()
    return redirect('community:list')

class PostDetail(DetailView):
    model = Post
    template_name_suffix = '_detail'

class PostLike(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
            #로그인 되어있는지 확인 
            # 로그인 해달라는 모달이나 알람 만들기 
        else:
            if 'post_id' in kwargs:
                post_id = kwargs['post_id']
                post = Post.objects.get(pk=post_id)
                user = request.user
                if user in post.like.all():
                    post.like.remove(user)
                else:
                    post.like.add(user)
            referer_url = request.META.get('HTTP_REFERER')
            #url 을 parse
            path = urlparse(referer_url).path
            return HttpResponseRedirect(path)

class PostUnlike(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
            #로그인 되어있는지 확인 
        else:
            if 'post_id' in kwargs:
                post_id = kwargs['post_id']
                post = Post.objects.get(pk = post_id)
                user = request.user
                if user in post.unlike.all():
                    post.unlike.remove(user)
                else:
                    post.unlike.add(user)
            referer_url = request.META.get('HTTP_REFERER')
            #url 을 parse
            path = urlparse(referer_url).path
            return HttpResponseRedirect(path)


class PostFavorite(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
            #로그인 되어있는지 확인 
        else:
            if 'post_id' in kwargs:
                post_id = kwargs['post_id']
                post = Post.objects.get(pk = post_id)
                user = request.user
                if user in post.favorite.all():
                    post.favorite.remove(user)
                else:
                    post.favorite.add(user)
            referer_url = request.META.get('HTTP_REFERER')
            #url 을 parse
            path = urlparse(referer_url).path
            return HttpResponseRedirect(path)


class PostFavoriteList(ListView):
    model = Post
    # template_name ='community/'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, '로그인을 먼저하세요')
            return HttpResponseRedirect('/')
        return super(PostFavoriteList, self).dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        user = self.request.user
        queryset = user.favorite_post.all()
        print(queryset)
        return queryset

class PostMyList(ListView):
    model = Post
    template_name = 'community/mypost.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, '로그인을 먼저하세요! ')
            return HttpResponseRedirect('/')
        return super(PostMyList,self).dispatch(request, *args, **kwargs)

def comment_create(request, post_id):

    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.created = timezone.now()
            comment.post = post
            comment.save()
            # return redirect('community:detail', post_id=post.id)
            # return HttpResponseRedirect('/community/detail/')
            return redirect('community:detail', pk=post_id)
    # else:
    #     form = CommentForm()
    # context = {'form': form}
    # return render(request, 'community/comment_form.html', context)
    # return render(request, 'community/comment_form.html', context)

def comment_update(request, comment_id):

    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('community:detail', post_id=comment.post.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.updated = timezone.now()
            comment.save()
            # return redirect('community:detail', post_id=comment.post.id)
            return redirect('community:detail', pk=comment.post_id)
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'community/comment_form.html', context)

def comment_delete(request, comment_id):

    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('community:detail', post_id=comment.post_id)
    else:
        comment.delete()
    return redirect('community:detail', pk=comment.post_id)


def search(request):
    posts = Post.objects.all().order_by('-id')

    q = request.POST.get('q', "")

    if q:
        posts = posts.filter(title__icontains=q)
        return render(request, 'community/search_post.html', {'posts': posts, 'q': q})

    else:
        return render(request, 'community/search_post.html')