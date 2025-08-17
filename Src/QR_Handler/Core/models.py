from django.db import models

# Create your models here.

class QRImages(models.Model):
    image = models.ImageField(upload_to='qr/')