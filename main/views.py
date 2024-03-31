from django.shortcuts import render, redirect
from .models import Task_1
from .forms import Task1Form

def index(request):
    tasks = Task_1.objects.order_by('id')[:1]
    return render(request, 'main/index.html', {'title': 'main page', 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = 'No errors'
    if request.method == 'POST':
        form = Task1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

        else:
            error = "The form is invalid"

    form = Task1Form()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
