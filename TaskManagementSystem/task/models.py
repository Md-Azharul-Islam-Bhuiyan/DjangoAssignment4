from django.db import models
from category.models import CategoryModel
class TaskModel(models.Model):
    task_title = models.CharField(max_length=50)
    taskDescription = models.TextField()
    category = models.ManyToManyField(CategoryModel)
    is_completed = models.BooleanField(default=False)
    Task_Assign_Date = models.DateField()
    
    def __str__(self):
        return self.task_title