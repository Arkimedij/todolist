from django.db import models

# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=90)
    taskdesc = models.TextField()
    time = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.taskTitle
    