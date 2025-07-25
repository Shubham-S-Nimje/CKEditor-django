from django.contrib import admin
from blog.models import blogPost

# Register your models here.
@admin.register(blogPost)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')