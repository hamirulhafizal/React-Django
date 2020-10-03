# todo/views.py

import os
import logging
from django.shortcuts import render
from rest_framework import viewsets  # add this
from .serializers import TodoSerializer  # add this
from .models import Todo  # add this
from src import settings
from django.http import HttpResponse


class TodoView(viewsets.ModelViewSet):  # add this
    serializer_class = TodoSerializer  # add this
    queryset = Todo.objects.all()  # add this


def todo(request):
    return render(request, 'Todo/home-1.html')


def react(request):
    index_file_path = os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')
    try:
        with open(index_file_path) as f:
            return HttpResponse(f.read())
    except FileNotFoundError:
        logging.exception('Production build of app not found')
