from django.urls import path
from  .  import views


urlpatterns = [
    path('', views.Principal, name='Principal'),
    path('home/', views.home, name='home'),
    path('Principal/', views.Principal, name='Principal'),
    path('header/', views.header, name='header'),
    path('Pintura/', views.Pintura, name='Pintura'),
    path('Frenos/', views.Frenos, name='Frenos'),
    path('Mantención/', views.Mantención, name='Mantención'),
    path('Formulario/', views.Formulario, name='Formulario'),
    path('Contacto/', views.Contacto, name='Contacto'),
    path('index/', views.index, name='index'),
    path('listadoSQL/', views.listadoSQL, name='listadoSQL'),
    path('crud/', views.crud, name='crud'),
    path('alumnosAdd/', views.alumnosAdd, name='alumnosAdd'),
    path('alumnos_del/<str:pk>', views.alumnos_del, name='alumnos_del'),
    path('alumnos_findEdit/<str:pk>', views.alumnos_findEdit, name='alumnos_findEdit'),
    path('alumnosUpdate', views.alumnosUpdate, name='alumnosUpdate'),
    path('alumnos_list/', views.alumnos_list, name='alumnos_list'),
    path('alumnos_add/', views.alumnos_add, name='alumnos_add'),
    path('alumnos_edit/', views.alumnos_edit, name='alumnos_edit'),
    


    
]