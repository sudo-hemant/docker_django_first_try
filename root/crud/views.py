from django.shortcuts import render
from rest_framework import generics, viewsets

from .models import Todo
from .serializers import TodoSerializer


# class ListTodo(generics.ListCreateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer


# class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Todo.objects.all()
#     serialzer_class = TodoSerializer


class TodoList(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer