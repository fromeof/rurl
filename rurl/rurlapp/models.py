from django.db import models

# Create your models here.
class url(models.Model):
    url_originale = models.URLField()
    url_raccourcie = models.CharField(max_length=20)