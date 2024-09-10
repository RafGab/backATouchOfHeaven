from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Memory
from .serializers import MemorySerializer


# Create and List memories
class MemoryListCreateView(generics.ListCreateAPIView):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Retrieve, Update, and Delete memories
class MemoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer
    permission_classes = [IsAuthenticated]
