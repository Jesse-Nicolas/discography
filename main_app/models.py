from django.db import models
from django.urls import reverse

# Create your models here.
class Vibe(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse("vibes_detail", kwargs={"pk": self.pk})




class Album(models.Model):
  title = models.CharField(max_length=100)
  artist = models.CharField(max_length=50)
  genre = models.CharField(max_length=50)
  description = models.TextField()
  released = models.IntegerField('year released', help_text='Enter a four-digit year')
  vibes = models.ManyToManyField(Vibe)

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
      return reverse("albums_detail", kwargs={"album_id": self.id})



# One album can have many listens (1:M)
class Listen(models.Model):
  date = models.DateField('Listening Date')
  impressions = models.TextField()
  album = models.ForeignKey(Album, on_delete=models.CASCADE)

  class Meta:
    ordering = ['-date']
  