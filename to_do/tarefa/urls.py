from django.urls import path
from . import views

urlpatterns = [
    path('tarefa/', views.index, name='tarefa')
]
