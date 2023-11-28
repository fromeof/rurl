from django.shortcuts import render, redirect
from .models import url
from django.http import HttpResponse
import uuid

# Create your views here.

def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new = url(lien=link, idd=uid)
        new.save()
        return HttpResponse(uid)
    
def success(request, pk):
    vrai_lien = url.objects.get(idd=pk)
    return redirect('http://'+vrai_lien.lien)