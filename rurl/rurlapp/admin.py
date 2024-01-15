from django.contrib import admin
from .models import Link, url_history
# Register your models here.

admin.site.register(Link)
admin.site.register(url_history)