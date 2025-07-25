from django.shortcuts import render
from blog.forms import CreatePostForm

# Create your views here.
def home(req):
    form = CreatePostForm()
    return render(req, 'blog/index.html',{'form':form})