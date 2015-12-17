from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Genre(models.Model):
    genre = models.CharField(max_length=200)


class Artist(models.Model):
    artist = models.CharField(max_length=200)


class Album(models.Model):
    album = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist)


class Song(models.Model):
    song = models.CharField(max_length=200)
    cd = models.ForeignKey(Album)


class Work(models.Model):
    work = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist)