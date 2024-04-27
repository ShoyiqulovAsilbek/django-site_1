from django.shortcuts import render
from.models import Post

def home_page(request):
    postlar = Post.objects.all()
    context = {
        'postlar': postlar
    }
    return render(request, 'index.html', context)
