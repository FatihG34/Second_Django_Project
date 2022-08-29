from django.urls import path

from blog.views import blog_add, blogs_cards, index


urlpatterns = [
    # path("", index, name='index'),
    path('', blogs_cards, name='home'),
    path('add/', blog_add, name='add'),
]
