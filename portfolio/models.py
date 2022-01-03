from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey, ManyToManyField

from account.models import Profile
from blog.models import Tag

# Create your models here.
class Project(models.Model):
    profile = ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=120)
    slug = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    source_link = models.CharField(max_length=200, null=True, blank=True)
    demo_link = models.CharField(max_length=200, null=True, blank=True)
    vote = models.IntegerField(default=1)
    state = models.BooleanField(default=False, choices=((False, 'Desactive'), (True, 'Active')))
    tags = ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title