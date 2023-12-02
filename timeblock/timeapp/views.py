from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from.models import Items
from .forms import TaskForm

# Create your views here.
def index(request):
    return render(request, "timeapp/index.html")
    # Home page is going to be the timeline


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('timeapp:task_list')
    else:
        form = TaskForm()
    return render(request, 'timeapp/create.html', {'form': form})

def task_list(request):
    tasks = Items.objects.all()
    return render(request, 'timeapp/task_list.html', {'tasks': tasks})