from django.urls import path   
from .import views
urlpatterns = [
    path('tovar/<uuid:id>/', views.tovar, name='tovar'),
]
