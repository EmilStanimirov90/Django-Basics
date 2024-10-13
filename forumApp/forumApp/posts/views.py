from datetime import datetime
from lib2to3.fixes.fix_input import context

from django.http import HttpResponse
from django.shortcuts import render, redirect

from forumApp.posts.forms import PostBaseForm
from forumApp.posts.models import Post


# from forumApp.posts.forms import PersonForm


# Create your views here.
def index(request):

    # form = PersonForm(request.POST or None)
    #
    # if request.method == 'POST':
    #     print(request.POST['person_name'])
    #
    #     if form.is_valid():
    #          print(form.cleaned_data['person_name'])

    context = {
        "my_form": "form",
        # "current_time": datetime.now(),
        # "person": {
        #     "age": 20,
        #     "height": 190,
        # },
        # "ids": ["123123", "fdgf32342", "3213ersdf"],
        # "some_text": "Hello my name is Ivan, and I am developer",
        # "some_text2": "",
        # "users": [ "ivan",
        #            "pesho",
        #            "maria",
        #            "gosho",
        #            "tosho",
        #            "magi",
        #             "geri"
        # ]
    }
    return render(request, 'base.html', context)

def dashboard(request):

    context = {
         "posts": Post.objects.all(),
        # [
        #     {
        #         "title":" Project name",
        #         "author": "Peter Parker",
        #         "content": "some explanations some explanations some explanations",
        #         "created_at":datetime.now(),
        #      },
        #     {
        #         "title": " Project name 1",
        #         "author": "",
        #         "content": "**some** explanations",
        #         "created_at": datetime.now(),
        #     },
        #     {
        #         "title": " Project name 2",
        #         "author": "Peter Parker",
        #         "content": "",
        #         "created_at": datetime.now(),
        #     },
        # ]
    }

    return render(request, 'posts/dashboard.html', context)

def add_post(request):
    form = PostBaseForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('dash')

    context = {
        'form': form

    }
    return render(request, 'posts/add-post.html', context)

