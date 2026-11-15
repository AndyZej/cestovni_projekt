

from core.models import ChatMessage
from django.contrib import admin


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
  list_display = ('sender', 'receiver', 'timestamp', 'is_read')
  list_filter = ('is_read', 'timestamp')