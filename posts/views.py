from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)


# def posts_list(request):
#     all_posts = Post.objects.all()
#     context = {
#         'all_posts': all_posts
#     }
#     return render(request, "posts/posts_list.html", context)


class PostListView(ListView):
    model = Post
    #categoryall = Category.objects.all()
    template_name = 'posts/home.html'  # <app>/<model>_<viewtype.html>
    #context_object_name = 'posts'
    ordering = '-date_posted'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-date_posted')
        context['categories'] = Category.objects.all()
        # And so on for more models
        return context


class UserPostListView(ListView):
    model = Post
    template_name = 'posts/user_posts.html'
    context_object_name = 'posts'
    ordering = '-date_posted'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class CategoryListView(ListView):
    model = Post
    template_name = 'posts/category_posts.html'
    context_object_name = 'posts'
    ordering = '-date_posted'
    paginate_by = 2

    def get_queryset(self):
        category = get_object_or_404(
            Category, category=self.kwargs.get('category'))
        return Post.objects.filter(category=category).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post

    template_name = 'posts/post_form.html'
    fields = ['title', 'content', 'image', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            False


def about(request):
    return render(request, 'posts/about.html')


def service(request):
    return render(request, 'posts/service.html')


# CRUD
# CREATE RETRIVE UPDATE DELETE
