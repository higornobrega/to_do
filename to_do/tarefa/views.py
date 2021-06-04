from django.shortcuts import redirect, render
from .models import TarefaBd
from .forms import ContentForm

def index(request):
    content = TarefaBd.objects.all()
    form = ContentForm()
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            form = form.save()
            return redirect('/')
                    
    context = {
        'contents': content,
        'form':form
    } 
    return render(request, 'lists.html', context)

def delete_content(request, id):
    deleteContent = TarefaBd.objects.get(id=id)
    deleteContent.delete()
    return redirect('/')