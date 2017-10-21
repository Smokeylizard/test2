from django.db import models
from datetime import date
from django.core.urlresolvers import reverse



# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    duedate = models.DateField(default=date.today, blank=True)

    def get_absolute_url(self):
        return reverse('todoapp:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title