from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MemoryView

router = DefaultRouter()
router.register(r'memories', MemoryView, basename='Memories')

urlpatterns = [
    path('', include(router.urls)),
]


# urlpatterns = router.urls
