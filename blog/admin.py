from django.contrib import admin

from blog.models import Blog


# Register your models here.
@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display = ['header', 'date']
