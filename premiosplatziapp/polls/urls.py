from django.urls import path
# EL PUNTO (.) INDICA QUE IMPORTA DEL MISMO DIRECTORIO LA CARPETA VIEWS.PY
from . import views

"""
DONDE: 
    path() == define la ruta de la URL
    '' == es la ruta raíz
    views.index == es la función index del módulo views.py
    name='index' == es el nombre o descripción de la ruta
"""

urlpatterns = [
    path('', views.index, name='index')
]