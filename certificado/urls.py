from django.urls import path
from . import views

urlpatterns = [
    path('solicitar_certificado/', views.solicitar_certificado, name='solicitar_certificado'),
    path('sucesso/', views.sucesso, name='sucesso'),
]
