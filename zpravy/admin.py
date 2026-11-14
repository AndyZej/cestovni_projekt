

from django.contrib import admin
from .models import ChatMessage


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
  list_display = ('sender', 'receiver', 'timestamp', 'message')
  search_fields = ('message', 'sender__username', 'receiver__username')