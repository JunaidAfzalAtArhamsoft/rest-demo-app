from django.shortcuts import render
from rest_framework import viewsets
from .models import Person, Task
from rest_framework import mixins
from rest_framework import generics
from .serializers import PersonSerializer, TaskSerializer
from rest_framework.views import APIView
from rest_framework import permissions


class PeronViewSet(viewsets.ModelViewSet):
    """
        Show and Create Person object
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAdminUser]


# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

# class PersonListCreateView(generics.ListAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer
#
#     permission_classes = [permissions.IsAdminUser]
#
#
