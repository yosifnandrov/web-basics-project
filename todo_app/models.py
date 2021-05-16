from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=45,blank=False)
    description = models.TextField(blank=False)
    is_done = models.BooleanField(blank=False, default=False)



