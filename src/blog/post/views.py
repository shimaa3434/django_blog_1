import email
from turtle import pos
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
# Create your views here.
def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'post/frontpage.html', {"posts": posts})

def caregory_detail(request, slug):
    category = get_object_or_404(Category, slug= slug)
    return render(request, "post/caregory_detail.html", {"category": category})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug= slug)
    if request.method == "POST":
        name = request.POST.get('name', '')
        comment = request.POST.get('comment', '')
        email = request.POST.get('email', '')
        if name and  comment and email:
            Comment.objects.create(
                post= post,
                name= name,
                email= email,
                comment= comment,
            )
            return redirect('post:post_detail', slug = post.slug)
    return render(request, 'post/post_detail.html', {"post": post})

