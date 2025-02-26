from django.shortcuts import render
from .models import Tovar
def  tovar(request, tovar_id):
    tovar = Tovar.objects.get(id=tovar_id)
    return render(request, 'tovar.html' , {'tovar': tovar})
