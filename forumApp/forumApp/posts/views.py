from datetime import datetime
from lib2to3.fixes.fix_input import context

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):

    context = {
        "current_time": datetime.now(),
        "person": {
            "age": 20,
            "height": 190,
        },
        "ids": ["123123", "fdgf32342", "3213ersdf"],
        "some_text": "Hello my name is Ivan, and I am developer",
        "some_text2": "",
        "users": [ "ivan",
                   "pesho",
                   "maria",
                   "gosho",
                   "tosho",
                   "magi",
                    "geri"
        ]
    }
    return render(request, 'base.html', context)

def dashboard(request):

    context = {
        "posts":[
            {
                "title":" Project name",
                "author": "Peter Parker",
                "content": "some explanations",
                "created_at":datetime.now(),
             },
            {
                "title": " Project name 1",
                "author": "",
                "content": "some explanations",
                "created_at": datetime.now(),
            },
            {
                "title": " Project name 2",
                "author": "Peter Parker",
                "content": "",
                "created_at": datetime.now(),
            },
        ]
    }

    return render(request, 'posts/dashboard.html', context)
