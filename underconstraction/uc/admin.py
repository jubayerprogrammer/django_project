from django.contrib import admin
from uc.models import *


# Register your models here.

@admin.register(UnderConstraction)
class underconstAdmin(admin.ModelAdmin):
    list_display = ["is_underconstraction","uc_note","uc_duration","uc_update"]
