from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import MemoryViewSet

urlpatterns = [
    path('', views.memory_list, name='memory_list'),
    path('create/', views.memory_create, name='memory_create'),
    path('update/<int:pk>/', views.memory_update, name='memory_update'),
    path('delete/<int:pk>/', views.memory_delete, name='memory_delete'),
]


router = DefaultRouter()
router.register(r'memories', MemoryViewSet)

urlpatterns = router.urls
