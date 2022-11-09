from django.contrib import admin
from .models import Album, Listen, Vibe

# Register your models here.
admin.site.register(Album)
admin.site.register(Listen)
admin.site.register(Vibe)