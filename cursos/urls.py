from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),   
    path('crearCurso/', views.crearCurso, name='crearCurso'),    
    path('editarCurso/<codigo>', views.editarCurso, name='editarCurso'),     
    path('eliminarCurso/<codigo>', views.eliminarCurso, name='eliminarCurso'),
]