from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('stones/', views.stones_index, name='index'),
    path('stones/<int:stone_id>', views.stones_detail, name='detail'),
    path('stones/create', views.StoneCreate.as_view(), name='stones_create'),
    path('stones/<int:pk>/update', views.StoneUpdate.as_view(), name='stones_update'),
    path('stones/<int:pk>/delete', views.StoneDelete.as_view(), name='stones_delete'),
    path('stones/<int:stone_id>/add_weilder', views.add_weilder, name='add_weilder'),
    path('movies/', views.MovieList.as_view(), name='movies_index'),
    path('movies/<int:pk>', views.MovieDetail.as_view(), name='movies_detail'),
    path('movies/create', views.MovieCreate.as_view(), name='movies_create'),
    path('movies/<int:pk>/update', views.MovieUpdate.as_view(), name='movies_update'),
    path('movies/<int:pk>/delete', views.MovieDelete.as_view(), name='movies_delete'),
]