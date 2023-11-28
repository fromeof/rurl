from django.db import models

# Create your models here.
class url(models.Model):
    lien = models.CharField(max_length=255)
    idd = models.CharField(max_length=10)