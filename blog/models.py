from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    blog_pic = models.ImageField(upload_to='blog_pics', blank=True)

    def __str__(self):
        return f"{self.title} "
