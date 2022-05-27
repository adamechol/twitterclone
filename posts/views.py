from http.client import HTTPResponse
import string
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

def index(request):
    # If the mehod is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # If the form is valid
        if form.is_valid():
            # yes, save
             form.save()
               
            # Redirect to Home
             return HttpResponseRedirect('/')
          
           
        else:
            # No, Show Error
            return HttpResponseRedirect(form.errors.as_json())
            
            
    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]
    
    form=PostForm()
    # show
    return render(request, 'post.html',
                    {'posts':posts})
    
def delete(request, post_id):
    post=Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')

def edit (request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("not valid")
        
    form = PostForm 
    return render (request, 'edit.html', {'post': post, 'form': form})

def My_like(request, post_id):
   post = Post.objects.get(id=post_id)
   post.likes += 1
   post.save()
   return HttpResponseRedirect('/')
