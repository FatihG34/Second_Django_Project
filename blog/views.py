from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import Blog
from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html')


def blogs_cards(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/dashboard.html', context)


def blog_add(request):
    form = BlogForm()  # boş form render edeceğiz
    if request.method == 'POST':
        # print(request.POST)
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {
        'form': form
    }
    return render(request, 'blog/blog_add.html', context)
 