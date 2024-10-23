from django.db import models

# Create your models here.

class Genre(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title




class VideoGame(models.Model):
    title = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    release_date = models.DateField()






