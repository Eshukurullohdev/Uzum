from django.db import models
from django.core.validators import RegexValidator

class Uzum(models.Model):
    img = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=100)
    sharh = models.CharField(max_length=100)
    bolib_tolash = models.IntegerField(default=0)
    skidka = models.IntegerField(default=0)
    narx = models.IntegerField(default=0)
    
    unique_id = models.CharField(
        max_length=90,
        validators=[
                RegexValidator(
                    regex=r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*])[^?&^]{-}$",
                    message='bunda $ @ ^ kiritib bolmaydi ',
                    code='hato_boldi'
                    
                )
            
        ],
        unique=True,
        null=True,
        blank=True,
        help_text="bu yerga hechnarsa kiritilmaydi",

    )
    
    def __str__(self):
        return self.description
    
