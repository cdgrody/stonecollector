from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('stones/', views.stones_index, name='index'),
    path('stones/<int:stone_id>', views.stones_detail, name='detail'),
]