from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    
class Item(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='items/')

    def __str__(self):
        return self.title

class Form(models.Model):
    body = models.TextField()
    name = models.CharField(max_length=255)
    email = models.EmailField()
    is_checked = models.BooleanField(default=False)
    status = models.CharField(max_length = 1, default = '0')
    sent_time = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return self.email
    