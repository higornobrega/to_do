from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('tarefas/', views.index),
    path('tarefas/delete/<slug:id>',views.delete_content),
    path('', RedirectView.as_view(url='tarefas/'))
]
