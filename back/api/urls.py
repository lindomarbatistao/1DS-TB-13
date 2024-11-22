from . import views
from django.urls import path

urlpatterns = [
    path('listar', views.listar_produtos),
]
