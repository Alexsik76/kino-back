from django.contrib import admin

from cinema.forms import MovieForm
from cinema.models import Viewer, Hall, Movie, Session, Seat, Booking, Country, Actor

class MovieAdmin(admin.ModelAdmin):
    form = MovieForm

admin.site.register(Movie, MovieAdmin)
admin.site.register([Viewer, Hall, Session, Seat, Booking, Country, Actor ])
