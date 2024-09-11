from django.shortcuts import render, redirect
from .models import Memory
from .form import MemoryForm
from rest_framework import viewsets
from .serializers import MemorySerializer


def memory_list(request):
    memories = Memory.objects.all()
    return render(request, 'memories/memory_list.html', {'memories': memories})


def memory_create(request):
    if request.method == 'POST':
        form = MemoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('memory_list')
    else:
        form = MemoryForm()
    return render(request, 'memories/memory_form.html', {'form': form})


def memory_update(request, pk):
    memory = Memory.objects.get(pk=pk)
    if request.method == 'POST':
        form = MemoryForm(request.POST, request.FILES, instance=memory)
        if form.is_valid():
            form.save()
            return redirect('memory_list')
    else:
        form = MemoryForm(instance=memory)
    return render(request, 'memories/memory_form.html', {'form': form})


def memory_delete(request, pk):
    memory = Memory.objects.get(pk=pk)
    if request.method == 'POST':
        memory.delete()
        return redirect('memory_list')
    return render(request, 'memories/memory_confirm_delete.html', {'memory': memory})


class MemoryViewSet(viewsets.ModelViewSet):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer
