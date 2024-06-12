from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('download/', views.download_file, name='download_file'),
    path('pad/', views.pad, name='pad'),
]