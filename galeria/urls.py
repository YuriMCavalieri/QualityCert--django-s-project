from django.urls import path
from galeria.views import imagemA1, index, imagem, imagemICP, imagemA3, cert, agenda

urlpatterns = [
     path('', index, name= 'index'),
    path('imagem/', imagem, name= 'imagem'),
    path('ICP/', imagemICP, name= 'ICP' ),
    path('A1/', imagemA1, name= 'A1'),
    path('A3/', imagemA3, name= 'A3'),
    path('cert', cert , name= 'cert'),
    path('agenda', agenda , name= 'agenda'),
]