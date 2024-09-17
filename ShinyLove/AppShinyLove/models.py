from django.db import models
from cloudinary.models import CloudinaryField

class Photo(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = CloudinaryField('image')
    vertical = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Fondo(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField('image')

    def __str__(self):
        return self.name