from django.shortcuts import render
from Uzum.models import Uzum
def  tovar(request, id):
    try: 
        detail = Uzum.objects.filter(unique_id=id).first()
    except Uzum.DoesNotExist:
        detail = None
    return render(request, 'tovar.html' , {'detail': detail} ,)
