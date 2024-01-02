from django.urls import path
from . import views



urlpatterns = [
    path('', views.Userview.as_view(), name="name"),
    
    
]