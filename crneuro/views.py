from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.db.models import Q
from django.http import JsonResponse
from .models import *

posts = profile.objects.all()
novells = TehProc.objects.all()
dang = Teh_use.objects.all()
cypher = Tasker.objects.all()
boom = tool_use.objects.all()
bah =  tool_n.objects.all()


def home(request):
    return render(request, 'crneuro/home.html', {'title': 'Логин'})


def tasks(request):
    context = {
        'novells': novells,
        'cypher': cypher,
        'dang': dang,
        'title': 'Задачи',
    }
    return render(request, 'crneuro/tasks.html', context=context)


def tools(request):
    context = {
        'boom': boom,
        'bah': bah,
        'novells': novells,
        'title': 'Инструменты'
    }
    return render(request, 'crneuro/tools.html', context=context)


def workers(request):
    context = {
        'posts': posts,
        'title': 'Рабочие',
    }
    return render(request, 'crneuro/workers.html', context=context)


def show_prof(request, prof_id):
    prof = get_object_or_404(profile, id=prof_id)

    context = {
        'prof': prof,
        'posts': posts,
        'title': 'Профиль',
    }

    return render(request, 'crneuro/prof.html', context=context)
