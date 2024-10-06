from lib2to3.fixes.fix_input import context

from django.http import HttpResponse
from django.shortcuts import render

from todo_app.models import Task


# Create your views here.
def index(request):
    title_filter = request.GET.get('title_filter', '')

    tasks = Task.objects.all()

    context = {
        'title_filter': title_filter,
        'tasks': tasks,
    }

    return render(request, 'tasks/index.html', context) #MIME TYPE   text html#


def add_view(request):
    return HttpResponse("<h1>ADD!</h1>") #MIME TYPE   text html#