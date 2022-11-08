from django.db import models
from django.urls import reverse

# Create your models here.
class Album(models.Model):
  title = models.CharField(max_length=100)
  artist = models.CharField(max_length=50)
  genre = models.CharField(max_length=50)
  description = models.TextField()
  released = models.IntegerField('year released', help_text='Enter a four-digit year')

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
      return reverse("albums_detail", kwargs={"album_id": self.id})
  