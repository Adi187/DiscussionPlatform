from django.contrib import admin

from .models import Room,Subject,Message

admin.site.register(Room)
admin.site.register(Subject)
admin.site.register(Message)