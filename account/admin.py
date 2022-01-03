from django.contrib import admin
from account.models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "username",
        "email",
        "state",
        "created_at",
    )
    list_filter = ("state",)
    search_fields = (
        "name",
        "username",
        "email",
    )


admin.site.register(Profile, ProfileAdmin)