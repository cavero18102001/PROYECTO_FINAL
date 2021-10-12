from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='home'),
    path('consulta/', views.inicio1, name='consulta'),
    path('consulta/<str:idConsulta>/', views.consulta, name='consulta'),
   # path('checkview', views.checkview, name='checkview'),
    path('enviar/<str:idConsulta>/', views.send, name='send'),
    path('getMessages/<str:idConsulta>/', views.getMessages, name='getMessages'),
]