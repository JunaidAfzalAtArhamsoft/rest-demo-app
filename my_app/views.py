from django.shortcuts import render
from rest_framework import viewsets
from .models import Person, Task
from .serializers import PersonSerializer, TaskSerializer


class PeronViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
