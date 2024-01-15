from django.db import models

class Collection(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    cover = models.CharField(max_length=1000)
    
    
    
class piece(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    year = models.IntegerField()
    piece_cover = models.CharField(max_length=1000)