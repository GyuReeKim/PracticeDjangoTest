from django.db import models

# Create your models here.
class Music(models.Model):
    title_1 = models.CharField(max_length=50)
    title_2 = models.CharField(max_length=50)
    image_url_1 = models.TextField()
    image_url_2 = models.TextField()

class Favor(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    pick = models.IntegerField()
    comment = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)