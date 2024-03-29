from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('create', views.create, name='create'),
    path('<str:pk>', views.success),
    path('history/', views.history, name='history')
]