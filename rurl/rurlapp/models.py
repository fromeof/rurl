from django.db import models

class Link(models.Model):
    lien = models.CharField(max_length=10000)
    idd = models.CharField(max_length=10)


    def __str__(self):
        return self.lien