from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Form(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    body = models.TextField()
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Material(models.Model):
    title = models.CharField(max_length = 255)
    text = models.TextField()
    author = models.CharField(max_length = 255)
    media  = models.ImageField()
    published = models.DateTimeField(auto_now_add = True)
    is_avctive = models.BooleanField(default = False)

