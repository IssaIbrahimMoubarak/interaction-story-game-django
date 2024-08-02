from django.urls import path
from . import views

urlpatterns = [
    path('', views.story_node, name='start'),  # URL racine qui affiche le premier nœud
    path('<str:key>/', views.story_node, name='story_node'),  # URL avec clé de nœud
]
