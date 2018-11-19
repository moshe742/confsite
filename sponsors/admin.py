from django.contrib import admin
from sponsors.models import Sponsor, SponsorLevel


def has_url(obj):
    return True if obj.url else False


def has_logo(obj):
    return True if obj.logo else False


class SponsorAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', has_url, has_logo]
    list_filter = ['name', 'level']


class SponsorLevelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']


admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(SponsorLevel, SponsorLevelAdmin)
