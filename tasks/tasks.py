from task_management.celery import app
from django.core.mail import send_mail

from . import models


class SendNotificationTask(app.Task):
    name = "send_notification_task"

    def run(self, task_id):
        try:
            task = models.Tasks.objects.get(id=task_id)
        except:
            return
        
        if task.status == models.Tasks.Status.DNE:
            print('Sending mail')


app.register_task(SendNotificationTask)