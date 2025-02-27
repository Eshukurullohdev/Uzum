from django.db import models
import uuid
class Tovars(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tavsif = models.CharField(max_length=100)
    imgs = models.ImageField(upload_to='images/')
    sharhi = models.IntegerField(default=0)
    asil_narx = models.IntegerField(default=0)
    skidkasi = models.IntegerField(default=0)
    foizi = models.IntegerField(default=0)