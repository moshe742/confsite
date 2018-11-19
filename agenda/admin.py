from django.contrib import admin
from agenda.models import Presentation, ContactInfoType, ContactInfo, Speaker, Track


class AgendaAdmin(admin.ModelAdmin):
    list_display = ['title', 'track', 'date', 'start_time', 'end_time']
    list_filter = ['title', 'track', 'date', 'start_time', 'end_time']


class ContactInfoTypeAdmin(admin.ModelAdmin):
    pass


class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_keynote']
    list_filter = ['name', 'is_keynote']


class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['speaker', 'info_type', 'info']
    list_filter = ['speaker', 'info_type', 'info']


admin.site.register(Presentation, AgendaAdmin)
admin.site.register(ContactInfoType, ContactInfoTypeAdmin)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(Track)
