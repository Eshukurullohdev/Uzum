from django.shortcuts import render
from .models import Tovars
from django.shortcuts import get_object_or_404
def  tovar(request, id):
    try:
         tovars = Tovars.objects.filter(id=id).exists()
    except Tovars.DoesNotExist:
        return render(request, '404.html')
    return render(request, 'tovar.html' , {'tovars': tovars})
