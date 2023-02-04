from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='name'),
    path('about/', views.about, name='about'),
    path('stones/', views.stones_index, name='index'),
]