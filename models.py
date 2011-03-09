from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class Priority(Category):
    class Meta:
        verbose_name_plural = "priorities"

class Type(Category):
    pass

class Status(Category):
    class Meta:
        verbose_name_plural = "statuses"

class Task(models.Model):
    """Trouble tickets"""
    title = models.CharField(max_length=100)
    submitted_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    description = models.TextField(blank=True)
    priority = models.ForeignKey(Priority)
    type = models.ForeignKey(Type)
    status = models.ForeignKey(Status)

    class Meta:
        ordering = ('submitted_date',)

    def __str__(self):
        return self.title