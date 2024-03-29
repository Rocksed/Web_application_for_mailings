from django.urls import path, include

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView

app_name = BlogConfig.name
urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('blog-detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog-detail/update/<int:pk>/', BlogUpdateView.as_view(), name='blog_updete'),

]
