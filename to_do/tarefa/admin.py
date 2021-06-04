from django.contrib import admin
from .models import TarefaBd

@admin.register(TarefaBd)

class TarefaAdmin(admin.ModelAdmin):
    list_display=['id', 'contents', 'date']