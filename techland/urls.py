from django.urls import path
from . import views

urlpatterns = [
    path('techland', views.home, name='home'),
    path('new_search1', views.new_search1, name='new_search1'),
    
]