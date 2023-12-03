from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Link
import uuid

def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link'].strip()
        uid = str(uuid.uuid4())[:5]
        nouveau = Link(lien=link, idd=uid)
        nouveau.save()
        return HttpResponse(uid)

def success(request, pk):
    vrai_lien = Link.objects.get(idd=pk)
    return redirect(vrai_lien.lien)