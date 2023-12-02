from django.db import models

# Create your models here.    
class Items(models.Model):
    TASK_TYPES = [('Work', 'Work'), ('Free Time', 'Free Time')] 

    title = models.CharField(max_length=300)
    task_type = models.CharField(max_length=10, choices=TASK_TYPES, default='Work')
    description = models.CharField(max_length=500, default='No Description')
    urgent = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.title