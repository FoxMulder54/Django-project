from django.contrib import admin
from portfolio.models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ("title",)}

    list_display = (
        "title",
        "profile",
        "slug",
        "state",
        "vote",
        "created_at",
    )

    list_filter = ("state",)

    filter_horizontal = ("tags",)

    search_fields = (
        "title",
        "description",
    )

    list_per_page = 4

    list_editable = ("state",)

    list_display_links = (
        "slug",
        "created_at",
    )


admin.site.register(Project, ProjectAdmin)