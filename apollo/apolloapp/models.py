from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    nomi = models.CharField(max_length=255)
    text = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.CharField(max_length=255)


    def __str__(self):
       return self.nomi
