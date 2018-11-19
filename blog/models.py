from django.db import models
from django.utils.translation import gettext as _

from common.models import Base


class Blog(Base):
    title = models.CharField(_('title'), max_length=200)
    body = models.TextField(_('body'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
