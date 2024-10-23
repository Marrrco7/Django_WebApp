from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.videogame_form,name='videogame_insert'),
    path('<int:id>/', views.videogame_form,name='videogame_update'),
    path('delete/<int:id>/',views.videogame_delete,name='videogame_delete'),
    path('list/',views.videogame_list,name='videogame_list')
]
