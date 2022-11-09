from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('albums/', views.albums_index, name='albums_index'),
  path('albums/<int:album_id>/', views.albums_detail, name='albums_detail'),
  path('albums/add/', views.AlbumAdd.as_view(), name='albums_add'),
  path('albums/<int:pk>/update', views.AlbumUpdate.as_view(), name='albums_update'),
  path('albums/<int:pk>/delete', views.AlbumDelete.as_view(), name='albums_delete'),
  path('albums/<int:album_id>/add_listen/', views.add_listen, name='add_listen'),
]