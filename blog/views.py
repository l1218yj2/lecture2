from django.shortcuts import render
from .models import blog
# Create your views here.
def blog_list(request):
    data = blog.objects.all()
    return render(request, 'index.html', context = {
        'blog_list':data,
    })

def blog_detail(request, pk= None):
    data = blog.objects.get(id=pk)
    return render(request, 'detail.html',context ={
        'blog':data,
    })

