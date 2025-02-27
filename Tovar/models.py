from django.db import models

class Tovars(models.Model):
    tavsif = models.CharField(max_length=100)
    imgs = models.ImageField(upload_to='images/')
    sharhi = models.IntegerField(default=0)
    asil_narx = models.IntegerField(default=0)
    skidkasi = models.IntegerField(default=0)
    foizi = models.IntegerField(default=0)