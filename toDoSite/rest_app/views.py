from django.shortcuts import render, get_object_or_404
from rest_framework import generics, viewsets, permissions
from .models import ToDo
from .serializers import ToDoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """
    API viewset for viewing todo instances.
    """
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
