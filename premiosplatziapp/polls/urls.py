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

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # EX: /polls/5/results/
    path('<int:pk>/results', views.ResultView.as_view(), name='results'),
    # EX: /polls/5/vote/
    path('<int:pk>/vote', views.vote, name='vote'),
    # EX: /polls/5/detail/
    path('<int:question_id>/detail', views.DetailView.as_view(), name='detail'),
]