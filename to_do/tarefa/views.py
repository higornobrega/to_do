from django.shortcuts import render
from .models import TarefaBd
from .forms import ContentForm

def index(request):
    content = TarefaBd.objects.all()
    form = ContentForm()
    context = {
        'contents': content,
        'form':form
    } 
    return render(request, 'lists.html', context)
