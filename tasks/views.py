from rest_framework.generics import *

from .models import Tasks
from .serializers import *
from .tasks import *

class AllTasksListCreateAPIView(ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerialzer

class TaskUpdateAPIView(UpdateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerialzer

    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.status == Tasks.Status.DNE:
            SendNotificationTask().apply_async(args=[instance.id])