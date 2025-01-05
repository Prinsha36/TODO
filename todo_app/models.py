from django.db import models

# Create your models here.
class Todo(models.Model): #PascalCase
    title = models.CharField(max_length=100) #varchar , char

    def __str__(self):
        return self.title
