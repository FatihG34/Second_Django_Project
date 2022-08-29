# PRECLASS SETUP

```bash
# CREATING VIRTUAL ENVIRONMENT
# windows
py -m venv env
# windows other option
python -m venv env
# linux / Mac OS
python3 -m venv env

# ACTIVATING ENVIRONMENT
# windows
.\env\Scripts\activate
# linux / Mac OS
source env/bin/activate

# PACKAGE INSTALLATION
# if pip does not work try pip3 in linux/Mac OS
pip install django
# alternatively python -m pip install django
pip install python-decouple
python -m django --version
django-admin startproject main .
```

add a gitignore file at same level as env folder

create a new file and name as .env at same level as env folder

copy your SECRET_KEY from settings.py into this .env file. Don't forget to remove quotation marks from SECRET_KEY

```
SECRET_KEY = django-insecure-)=b-%-w+0_^slb(exmy*mfiaj&wz6_fb4m&s=az-zs!#1^ui7j
```

go to settings.py, make amendments below

```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
```

go to terminal

```bash
py manage.py migrate
py manage.py runserver
```

click the link with CTRL key pressed in the terminal and see django rocket.

go to terminal, stop project, add app

```
py manage.py startapp blog
```

go to settings.py and add 'blog' app to installed apps and add below lines

```python
import os
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') or
MEDIA_ROOT = BASE_DIR / 'media/'
MEDIA_URL = '/media/'
```
to see the picture on browser.
go to main/urls.py

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

create these folders at project level as /media/

go to blog/models.py

```python
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    blog_pic = models.ImageField(upload_to='blog_pics', blank=True)

    def __str__(self):
        return f"{self.title} "


```

go to terminal

```bash
pip install pillow
pip freeze > requirements.txt
py manage.py makemigrations
py manage.py migrate
python manage.py createsuperuser
```

navigate to admin panel and show that student model does not exist

go to blog/admin.py

```python
from django.contrib import admin

from .models import Blog
# Register your models here.
admin.site.register(Blog)
```

##templates


create template folder as blog/templates/blog

base.html

```html
<!DOCTYPE html>
{% load static %}
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
   <!-- CSS only -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
    <title>Django Blog APP</title>
    <!-- <link rel="stylesheet" href="../static/css/style.css" /> -->
    <link rel="stylesheet" href="{% static 'blog/css/style.css' %}" />
  </head>
  <body>
    {% block container %}{% endblock container %}

    <script
      src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
      integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
      crossorigin="anonymous"
    ></script>
    <script src="{% static 'fscohort/js/timeout.js' %}"></script>
  </body>
</html>
```

index.html

```html
{% extends "blog/base.html" %} {% block container %}
<h1>Home Page</h1>

<h3>Blog App</h3>

{% endblock container %}

```

go to blog/views.py

```python
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

    
```

go to main/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
```

go to BLOG/urls.py

```python
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='home'),
]
```


/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
/*/                                     /*/
/*/         CRUD  - READ(GET)           /*/
/*/                                     /*/
/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/


go to blog/views.py
```python
from .models import Blog

def blogs_cards(request):
    blogs  = Blog.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/dashboard.html', context)
```


go to blog/urls.py
```python
from django.urls import path
from .views import blogs_cards

urlpatterns = [

    path('',blogs_cards , name='home'),
]
```


index.html
```html


{% extends "blog/base.html" %} {% block container %}
<h1>Home Page</h1>

<h3>Blog App</h3>
<div class="container d-flex flex-wrap gap-5">

  {% for blog in blogs%}
  <div class="card" style="width: 18rem;">
    <img class="card-img-top" src="{{blog.blog_pic.url}}" alt="Card image cap">
    <div class="card-body">
      <h5 class="card-title">{{blog.title}}</h5>
      <p class='text-muted'>{{blog.created_date}}</p>
      <p class="card-text">{{blog.description|truncatechars:50}}</p>
      <a href="#" class="btn btn-primary">Detail</a>
    </div>
  </div>
  
  {%endfor%}
</div>


{% endblock container %}
```


/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
/*/                                     /*/
/*/         CRUD  - CREATE (POST)       /*/
/*/                                     /*/
/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/


go to blog/forms.py
```python
from django import forms
from .models import Blog
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','description','blog_pic')
        widgets = {

        'title':forms.TextInput(attrs={'class': 'form-control  row mb-3','placeholder':'Title'}),
        'description':forms.TextInput(attrs={'class': 'form-control  row mb-3','placeholder':'Description'})
      

        }

        labels = {"title": "Title", "description":"Description"}

```


go to blog/views.py
```python
from django.shortcuts import render,redirect
from .forms import BlogForm

def blog_add(request):
    form = BlogForm() # boş form render edeceğiz
    if request.method == 'POST':          
        print(request.POST)				   
        form = BlogForm(request.POST)   
        if form.is_valid():				   
            form.save()
            return redirect("home")					   
    context = {
        'form' : form
    }
    return render(request, 'blog/blog_add.html', context)

```


go to blog/urls.py
```python
from django.urls import path
from .views import blogs_cards,blog_add

urlpatterns = [

    path('',blogs_cards , name='home'),
     path('add/',blog_add , name='add'),
]
```