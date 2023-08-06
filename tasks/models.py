from django.db import models

class Tasks (models.Model):
    class Status(models.TextChoices):
        PEN = 'pending', 'Pending'
        DNE = 'done', 'Done'

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PEN)
    due_date = models.DateTimeField()

