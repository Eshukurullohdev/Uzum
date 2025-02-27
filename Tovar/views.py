from django.shortcuts import render

def  tovar(request, tovar_id):
    return render(request, 'tovar.html' , {'tovar': tovar})
