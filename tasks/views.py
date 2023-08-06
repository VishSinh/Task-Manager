from rest_framework.generics import *

from .models import Tasks
from .serializers import *

class AllTasksListCreateAPIView(ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerialzer

class TaskUpdateAPIView(UpdateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskUpdateSerializer