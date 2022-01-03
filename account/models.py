from django.db import models
from django.db.models.fields.related import OneToOneField
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.
class Profile(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE)
    name =models.CharField(max_length=80)
    username = models.CharField(max_length=80, unique=True, null=True, blank=True)
    email = models.EmailField(max_length=120, null=True, blank=True, unique=True)
    head_line = models.CharField(max_length=200, null=True, blank=True)
    about_as = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="profiles/", default="profiles/default.png")
    resume_link = models.CharField(max_length=200, null=True, blank=True)
    linkden_link = models.CharField(max_length=200, null=True, blank=True)
    facebook_link =models.CharField(max_length=200, null=True, blank=True)
    website_link = models.CharField(max_length=200, null=True, blank=True)
    youtub_link = models.CharField(max_length=200, null=True, blank=True)
    state = models.BooleanField(default=False, choices=((False, 'Desactive'), (True, 'Active')))
    id = models.UUIDField(primary_key = True, unique=True, default = uuid4, editable = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
