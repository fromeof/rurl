from django.db import models

class Link(models.Model):
    lien = models.CharField(max_length=10000)
    idd = models.CharField(max_length=10)


    def __str__(self):
        return self.lien
    
class url_history(models.Model):
    id = models.AutoField(primary_key=True)
    original_url = models.URLField()
    short_url = models.URLField()

    def __str__(self):
        return f"{self.id} - {self.original_url}"