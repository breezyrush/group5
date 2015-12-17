from django.shortcuts import render
from django.http import *
from django.views.generic import View
from django.contrib import auth
from models import *
from forms import *
import json
from django.utils import timezone
import datetime
from django.db import connection
# Create your views here.


def index(request):
    form = LoginForm()
    return render(request, 'index.html', {'form': form})


class Login(View):
    def post(self, request):
        form = LoginForm(self.request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponse('Logged In!')
            else:
                return HttpResponse('Invalid pasword/username!')
        else:
            return HttpResponse('Please fill out required forms!')


def addGenreForm(request):
    return render(request, 'add_genre.html')


def addGenre(request):
    genre = request.GET['genre']
    query = Genre(genre=genre)
    query.save()
    return render(request, 'add_genre.html')

class deleteAlbum(request):

    def get(self, request):
        album_id = request.GET['album_id']
        query = Album.objects.get(id=subject_id)
        query.delete()
        return HttpResponse()

class UpdateGenre(View):
    def post(self, request):
        return HttpResponse()

class AddArtist(View):
    def post(self, request):
        # Get data
        artist_name = request.POST['artist_name']
        genre_id = request.POST['genre_id']
        # Get instance
        genre_instance = Genre.objects.get(id=genre_id)
        # Check redundancy
        redundant = Artist.objects.filter(artist_name__iexact=artist_name, genre=genre_instance)
      
        if len(redundant) == 0:
            query = Artist(artist_name=artist_name, genre=genre_instance)
            query.save()

class DeleteArtist(View):
    def post(self, request):
        artist_id = request.POST['artist_id']
        query = Artist.objects.get(id=artist_id)
        query.delete()
        return HttpREsponse()

class UpdateArtist(View)
    def post(self, request):
        genre_id = request.POST['genre_id']
        artist_id = request.POST['artist_id']
        artist_name = request.POST['artist_name']

        # Check redundancy
        redundant = Artist.objects.filter(artist_name__iexact=artist_name, genre=genre_instance)
      
        if len(redundant) == 0:
            query = Artist(artist_name=artist_name, genre=genre_instance)
            query.save()
            data = dict()
            data['error'] = False 
            return HttpResponse(json.dumps(data), content_type="application/json")
        else:
            data = dict()
            data['error'] = True
            return HttpResponse(json.dumps(data), content_type="application/json")


