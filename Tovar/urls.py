from django.urls import path   
from .import views
urlpatterns = [
    path('tovar/<str:tovar_id>/', views.tovar, name='tovar'),
]
