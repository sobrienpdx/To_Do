from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required #import this for @login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from .models import ToDo
from django.urls import reverse

# Create your views here.


def index(request):
    to_do_list = ToDo.objects.all()
    context = {'to_do_list': to_do_list}
    return render(request, 'toDoApp/index.html', context)
    # return HttpResponse('ok. def index got called on the views page because urls.py at the app level has a path called views.index')

@login_required #makes it so that if the user isn;t logged in they get re-directed to the login page
def add(request):
    if request.method == 'POST':
        text = request.POST['to_do_text']
        ToDo(to_do_text=text).save()
    return HttpResponseRedirect(reverse('toDoApp:index'))


def delete(request, pk):
        # access the instance of ToDo class with the id of "id"
    # to_delete = ToDo.objects.filter(id=pk)
    get_object_or_404(ToDo, pk=pk).delete()
    # print(id)
    return HttpResponseRedirect(reverse('toDoApp:index'))


def mark_done(request, pk):
    to_do = get_object_or_404(ToDo, pk=pk)
    # to_do = ToDo.objects.get(pk=pk)
    to_do.completed = (not to_do.completed)
    to_do.save()
    # ToDo(to_do_text=f'you tried to mark item {pk} done.').save()
    return HttpResponseRedirect(reverse('toDoApp:index'))


def another(request):
    return HttpResponse('This is another_page')
