from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from agenda.models import Presentation, ContactInfoType, ContactInfo, Speaker, Track


class AgendaAdmin(admin.ModelAdmin):
    list_display = ['title', 'track', 'date', 'start_time', 'end_time']
    list_filter = ['title', 'track', 'date', 'start_time', 'end_time']


class ContactInfoTypeAdmin(admin.ModelAdmin):
    pass


class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_keynote']
    list_filter = ['user', 'is_keynote']


class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['speaker', 'info_type', 'info']
    list_filter = ['speaker', 'info_type', 'info']


admin.site.register(Presentation, AgendaAdmin)
admin.site.register(ContactInfoType, ContactInfoTypeAdmin)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(Track)
