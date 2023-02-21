from django.urls import path
from .views import index, updateTask, deleteTask


urlpatterns = [
    path('', index, name='list'),
    path('update_task/<int:pk>', updateTask, name='update'),
    path('delete/<int:pk>', deleteTask, name='delete'),
]