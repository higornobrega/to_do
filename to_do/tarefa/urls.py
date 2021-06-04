from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('tarefas/', views.index),
    path('', RedirectView.as_view(url='tarefas/'))
]
