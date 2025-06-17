from django.contrib import admin
from .models import TaskLog

@admin.register(TaskLog)
class TaskLogAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'message')
    ordering = ('-created_at',)
