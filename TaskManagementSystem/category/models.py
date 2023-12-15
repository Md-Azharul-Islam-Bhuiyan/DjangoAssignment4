from django.db import models
# from task.models import TaskModel

class CategoryModel(models.Model):
    category_name = models.CharField(max_length=50)
    # task = models.ManyToManyField(TaskModel)

    def __str__(self):
        return self.category_name