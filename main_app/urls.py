from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('albums/', views.albums_index, name='albums_index'),
  path('albums/<int:album_id>/', views.albums_detail, name='albums_detail'),
  path('albums/add/', views.AlbumAdd.as_view(), name='albums_add'),
  path('albums/<int:pk>/update', views.AlbumUpdate.as_view(), name='albums_update'),
  path('albums/<int:pk>/delete', views.AlbumDelete.as_view(), name='albums_delete'),
  path('albums/<int:album_id>/add_listen/', views.add_listen, name='add_listen'),
  path('vibes/create', views.VibeCreate.as_view(), name='vibes_create'),
  path('vibes/<int:pk>/', views.VibeDetail.as_view(), name='vibes_detail'),
  path('vibes/', views.VibeList.as_view(), name='vibes_index'),
  path('vibes/<int:pk>/update/', views.VibeUpdate.as_view(), name='vibes_update'),
  path('vibes/<int:pk>/delete/', views.VibeDelete.as_view(), name='vibes_delete'),
  path('albums/<int:album_id>/assoc_vibe/<int:vibe_id>/', views.assoc_vibe, name='assoc_vibe'),
  path('albums/<int:album_id>/disassoc_vibe/<int:vibe_id>/', views.disassoc_vibe, name='disassoc_vibe'),
  path('accounts/signup/', views.signup, name='signup'),
]