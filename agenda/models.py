from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

from common.models import Base


class Track(Base):
    name = models.CharField(_('name'), max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Track')
        verbose_name_plural = _('Tracks')


class Presentation(Base):
    title = models.CharField(_('title'), max_length=500)
    abstract = models.TextField(_('abstract'))
    selected = models.BooleanField(_('is_selected'), default=False)
    date = models.DateField(_('date'), null=True)
    start_time = models.TimeField(_('start'), null=True)
    end_time = models.TimeField(_('end'), null=True)
    track = models.ForeignKey(Track, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{0}: {1}, {2}, {3} - {4}'.format(self.track, self.title, self.date,
                                                 self.start_time, self.end_time)

    class Meta:
        verbose_name = _('Agenda')
        verbose_name_plural = _('Agenda')


class ContactInfoType(Base):
    name = models.CharField(_('name'), max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact info type'
        verbose_name_plural = 'Contact info types'


class Speaker(Base):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_keynote = models.BooleanField(_('is keynote'), default=False)
    sessions = models.ManyToManyField(Presentation, related_name='speakers')
    bio = models.TextField(_('short bio'))
    picture = models.ImageField(_('picture'), null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        verbose_name = 'Speaker'
        verbose_name_plural = 'Speakers'


class ContactInfo(Base):
    info_type = models.ForeignKey(ContactInfoType, on_delete=models.CASCADE)
    info = models.CharField(_('info'), max_length=200)
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE, related_name='contact_info')

    def __str__(self):
        return '{0}: {1}- {2}'.format(self.speaker, self.info_type, self.info)

    class Meta:
        verbose_name = _('Contact info')
        verbose_name_plural = _('Contact info')
