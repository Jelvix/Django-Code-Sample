from django.contrib import admin
from .models import Room, Message
# Register your models here.


class RoomAdmin(admin.ModelAdmin):
    list_display = ('title', 'creation_date', 'update_date')


admin.site.register(Room, RoomAdmin)
admin.site.register(Message)
