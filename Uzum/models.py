from django.db import models


class Uzum(models.Model):
    img = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=100)
    sharh = models.CharField(max_length=100)
    bolib_tolash = models.IntegerField(default=0)
    skidka = models.IntegerField(default=0)
    narx = models.IntegerField(default=0)
    
    def __str__(self):
        return self.description
    
