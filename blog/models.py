from django.db import models
from django.utils.text import slugify
from django.db.models.fields import CharField, DateTimeField, IntegerField, TextField, SlugField
from django.urls import reverse
from django.db.models.fields.related import ForeignKey, ManyToManyField

from account.models import Profile

LIST_STATE = (
        (0, "Draft"),
        (1, "Published")
    )

# Create your models here.
class Article(models.Model):
    profile = ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    state = IntegerField(default=0, choices=LIST_STATE)
    title = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True, db_index=True, null=True, blank=True)
    description = TextField(null=True)
    category = ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    tags = ManyToManyField('Tag')
    picture = models.ImageField(null=True, upload_to='articles/')
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("show_article", kwargs={"slug": self.slug})


class Category(models.Model):
    class Meta:
        verbose_name = "Categorie"

    name = CharField(max_length=20)
    state = IntegerField(default=0, choices=LIST_STATE)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = CharField(max_length=20)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
