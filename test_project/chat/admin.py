from django.contrib import admin

from .models import Chat


class AdminChat(admin.ModelAdmin):
    list_display = ('from_user', 'message', 'has_seen', 'created_on')

admin.site.register(Chat, AdminChat)