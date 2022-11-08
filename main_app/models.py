from django.db import models

# Create your models here.
class Album(models.Model):
  title = models.CharField(max_length=100)
  artist = models.CharField(max_length=50)
  genre = models.CharField(max_length=50)
  description = models.TextField()
  released = models.DateField('date released')

  def __str__(self):
    return self.title