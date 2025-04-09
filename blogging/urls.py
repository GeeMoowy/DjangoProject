from django.urls import path

from blogging.views import BlogsView, BlogsCreateView, BlogDetailView, BlogUpdateView, BlogDeleteViews

app_name = 'blogs'

urlpatterns = [
    path('', BlogsView.as_view(), name='blogs'),
    path('add_blog/', BlogsCreateView.as_view(), name='add_blog'),
    path('<int:pk>/update_blog/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog_detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('<int:pk>/blog_delete', BlogDeleteViews.as_view(), name='blog_delete'),
]