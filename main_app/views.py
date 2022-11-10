from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Album, Vibe
from .forms import ListenForm

# public
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('albums_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

# auth protected
@login_required
def albums_index(request):
  albums = request.user.album_set.all()
  return render(request, 'albums/index.html', { 'albums': albums })

@login_required
def albums_detail(request, album_id):
  album = Album.objects.get(id=album_id)
  unassigned_vibes = Vibe.objects.exclude(id__in = album.vibes.all().values_list('id'))
  listen_form = ListenForm()
  return render(request, 'albums/detail.html', { 'album': album, 'listen_form': listen_form, 'vibes': unassigned_vibes })

@login_required
def add_listen(request, album_id):
  form = ListenForm(request.POST)
  if form.is_valid():
    new_listen = form.save(commit=False)
    new_listen.album_id = album_id
    new_listen.save()
  return redirect('albums_detail', album_id=album_id)

@login_required
def assoc_vibe(request, album_id, vibe_id):
  Album.objects.get(id=album_id).vibes.add(vibe_id)
  return redirect('albums_detail', album_id=album_id)

@login_required
def disassoc_vibe(request, album_id, vibe_id):
  Album.objects.get(id=album_id).vibes.remove(vibe_id)
  return redirect('albums_detail', album_id=album_id)

class AlbumAdd(LoginRequiredMixin, CreateView):
  model = Album
  fields = ['title', 'artist', 'genre', 'description', 'released']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class AlbumUpdate(LoginRequiredMixin, UpdateView):
  model = Album
  fields = ['description', 'genre']

class AlbumDelete(LoginRequiredMixin, DeleteView):
  model = Album
  success_url = '/albums/'

class VibeCreate(LoginRequiredMixin, CreateView):
  model = Vibe
  fields = '__all__'

class VibeList(LoginRequiredMixin, ListView):
  model = Vibe

class VibeDetail(LoginRequiredMixin, DetailView):
  model = Vibe

class VibeUpdate(LoginRequiredMixin, UpdateView):
  model = Vibe
  fields = '__all__'

class VibeDelete(LoginRequiredMixin, DeleteView):
  model = Vibe
  success_url = '/vibes/'


