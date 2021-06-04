from django.shortcuts import render
from .models import TarefaBd

def index(request):
    content = TarefaBd.objects.all()
    context = {
        'contents': content
    } 

    print (content)

    return render(request, 'lists.html', context)
