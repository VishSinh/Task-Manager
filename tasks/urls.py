from django.urls import path

from .views import *

app_name = 'tasks'

urlpatterns = [
    path('', AllTasksListCreateAPIView.as_view(), name='task'),
    path('update/<int:pk>/', TaskUpdateAPIView.as_view(), name = 'task_update'),
]