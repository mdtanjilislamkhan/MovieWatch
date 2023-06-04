from django.db import models


class Movie(models.Model):
    imdb_id = models.CharField(max_length=50)
    title = models.CharField(max_length=25)
    year=models.IntegerField()
    image=models.CharField(max_length=10000)
    averageRating=models.CharField(max_length=10)
    def __str__(self) -> str:
        return self.title
    
class Top_Movies(models.Model):
    imdb_id = models.CharField(max_length=50)
    title = models.CharField(max_length=25)
    year=models.IntegerField()
    image=models.CharField(max_length=10000)
    averageRating=models.CharField(max_length=10)
    def __str__(self) -> str:
        return self.title