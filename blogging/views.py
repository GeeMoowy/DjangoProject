from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView

from blogging.forms import BlogForm
from blogging.models import Blog


class BlogsView(ListView):
    model = Blog
    template_name = 'blogging/blogs.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.all()


class BlogsCreateView(CreateView):
    template_name = 'blogging/add_blog.html'
    form_class = BlogForm
    success_url = reverse_lazy('blogs:blogs')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'sign_of_publication')
    template_name = 'blogging/add_blog.html'
    success_url = reverse_lazy('blogs:blogs')


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogging/blog_detail.html'
    context_object_name = 'blog'


class BlogDeleteViews(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs:blogs')
