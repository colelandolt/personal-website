from django.contrib import admin

from .models import Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'active', 'timestamp']
    search_fields = ['email', 'name']
    readonly_fields = ['timestamp']
    list_filter = ['active', 'timestamp']

admin.site.register(Subscriber, SubscriberAdmin)
