from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
from django.conf import settings

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

    def get_success_url(self):
        return reverse('blogs:blog_detail', args=[self.kwargs.get('pk')])


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogging/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()

        if self.object.views_count == 100:
            self.send_notification()

        return self.object

    def send_notification(self):
        subject = 'Блог достиг 100 просмотров!'
        message = f'Ваш блог "{self.object.title}" достиг 100 просмотров.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['kovylek.ul@gmail.com']

        send_mail(subject, message, email_from, recipient_list)


class BlogDeleteViews(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs:blogs')
