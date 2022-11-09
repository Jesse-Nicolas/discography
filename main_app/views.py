from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Album, Vibe
from .forms import ListenForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def albums_index(request):
  albums = Album.objects.all()
  return render(request, 'albums/index.html', { 'albums': albums })

def albums_detail(request, album_id):
  album = Album.objects.get(id=album_id)
  unassigned_vibes = Vibe.objects.exclude(id__in = album.vibes.all().values_list('id'))
  listen_form = ListenForm()
  return render(request, 'albums/detail.html', { 'album': album, 'listen_form': listen_form, 'vibes': unassigned_vibes })

class AlbumAdd(CreateView):
  model = Album
  fields = ['title', 'artist', 'genre', 'description', 'released']

class AlbumUpdate(UpdateView):
  model = Album
  fields = ['description', 'genre']

class AlbumDelete(DeleteView):
  model = Album
  success_url = '/albums/'

def add_listen(request, album_id):
  form = ListenForm(request.POST)
  if form.is_valid():
    new_listen = form.save(commit=False)
    new_listen.album_id = album_id
    new_listen.save()
  return redirect('albums_detail', album_id=album_id)

class VibeCreate(CreateView):
  model = Vibe
  fields = '__all__'

class VibeList(ListView):
  model = Vibe

class VibeDetail(DetailView):
  model = Vibe

class VibeUpdate(UpdateView):
  model = Vibe
  fields = '__all__'

class VibeDelete(DeleteView):
  model = Vibe
  success_url = '/vibes/'

def assoc_vibe(request, album_id, vibe_id):
  Album.objects.get(id=album_id).vibes.add(vibe_id)
  return redirect('albums_detail', album_id=album_id)