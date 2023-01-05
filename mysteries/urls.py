from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create', views.create_mystery, name="create_mystery")
]
