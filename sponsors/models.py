from django.db import models
from django.utils.translation import gettext as _

from common.models import Base


class SponsorLevel(Base):
    name = models.CharField(_('name'), max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sponsor level'
        verbose_name_plural = 'Sponsor levels'


class Sponsor(Base):
    name = models.CharField(_('name'), max_length=200)
    logo = models.ImageField(_('logo'))
    url = models.URLField()
    level = models.ForeignKey(SponsorLevel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return '{0}, {1}'.format(self.name, self.level)

    class Meta:
        verbose_name = 'Sponsor'
        verbose_name_plural = 'Sponsors'
