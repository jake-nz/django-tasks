from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=100)

class Priority(models.Model):
	pass

class Type(models.Model):
	pass

class Status(models.Model):
	pass

class Task(models.Model):
    """Trouble tickets"""
    title = models.CharField(max_length=100)
    submitted_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    submitter = models.ForeignKey(User, related_name="submitter")
    assigned_to = models.ForeignKey(User)
    description = models.TextField(blank=True)
    priority = models.ForeignKey(Priority)
    type = models.ForeignKey(Type)
    status = models.ForeignKey(Status)

    class Meta:
        ordering = ('submitted_date',)

    def __str__(self):
        return self.title