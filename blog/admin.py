from django.contrib import admin

# Register your models here.
from .models import Article, Category, Tag

class ArticleAdmin(admin.ModelAdmin):
   list_display = ("title", "slug", "state", "category", "created_at")
   list_filter = ("state", "category")
   prepopulated_fields = {"slug": ("title",)}
   list_per_page = 4
   
admin.site.register(Article, ArticleAdmin)

admin.site.register([Category, Tag])