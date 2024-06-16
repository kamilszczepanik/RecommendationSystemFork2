from django.contrib import admin
from .models import Movies
from .models import Directors, Directorsdetails
from .models import Genre, Genredetails
from .models import Moviecast, Moviecastdetails
# Register your models here.

admin.site.register(Movies)
admin.site.register(Directors)
admin.site.register(Directorsdetails)
admin.site.register(Genre)
admin.site.register(Genredetails)
admin.site.register(Moviecast)
admin.site.register(Moviecastdetails)