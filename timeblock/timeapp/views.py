from django.shortcuts import render
from django.http import HttpResponse
from.models import ToDoList, Items

# Create your views here.
def index(request):
    return render(request, "timeapp/index.html")
    # Home page is going to be the timeline

def list_file(reponse, id):
    ls = ToDoList.objects.get(id=id)
    return HttpResponse("<h1>%s<h1>" %ls.name)    
# Needs to be a seperate page that shows lists 'Work' and 'Freetime'


# Needs to be an add tast page for each of these
def create(request):
    return render(request, "timeapp/create.html")

# A seperate page to view the list in a Eisenhowers Matrix