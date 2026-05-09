from django.contrib import admin
from core.models import Profile

# Register your models here.
@admin.register(Profile)
class profile_admin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.fields]
    