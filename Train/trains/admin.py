from django.contrib import admin
from .models import Train


# Register your models here.

@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ["data", "deadline", "deadline_failed_time", "is_active"]
    list_editable = ["deadline", "is_active"]
    list_filter = ["is_active"]
