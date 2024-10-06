from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import request
from django.urls import reverse, reverse_lazy

from urlsAndViews.departments.models import Department


# Create your views here.
def index(request):
    url = reverse('redirect-to-view')
    url_lazy = reverse_lazy('redirect-to-view')
    return HttpResponse(f'{url_lazy}')
    # return HttpResponse('<h1>Hello World!</h1>')

def view_with_args_kwargs(request, *args, **kwargs):
    return HttpResponse(f'<h1>Args: {args} Kwargs: {kwargs}</h1>')


def view_with_int_pk(request, pk):
    return HttpResponse(f'<h1>INT pk with pk: {pk}</h1>', content_type='text/plain')

def view_with_slug(request, slug):
    department = get_object_or_404(Department.objects.get(slug=slug))

    # return HttpResponseNotFound()
    # return HttpResponse(f'<h1>Department form Slug: {department}</h1>')

def view_with_name(request, variable):
    raise Http404

    # return HttpResponse(f'<h1>Variable: {variable}</h1>')
    # return render(request,'templates/departments/name_template.html', {"variable": variable})

def show_archive(request, year):
    return HttpResponse(f'<h1>Archive year is {year}</h1>')

def redirect_to_softuni(request):
    return redirect('https://softuni.bg')

def redirect_to_view(request):
    # return redirect('http://localhost:8000/') breaks abstraction
    # return redirect(index) breaks
    return redirect('home') # BEST OPTION
