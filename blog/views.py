from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from blog.models import Blog


# Create your views here.

class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ['header', 'content', 'img']
    success_url = reverse_lazy('blog:blog_list')


class BlogUpdateView(UpdateView):
    model = Blog
