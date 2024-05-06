from django.contrib import admin

from .models import Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'timestamp']
    search_fields = ['email', 'name']
    readonly_fields = ['timestamp']
    list_filter = ['timestamp']

admin.site.register(Subscriber, SubscriberAdmin)
