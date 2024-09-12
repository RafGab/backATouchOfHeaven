from django.shortcuts import render, redirect
from .models import Memory
from rest_framework import viewsets
from .serializers import MemorySerializer


class MemoryView(viewsets.ModelViewSet):
    serializer_class = MemorySerializer
    queryset = Memory.objects.all()
