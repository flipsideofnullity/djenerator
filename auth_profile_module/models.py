from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.conf import settings
from django.core.urlresolvers import reverse
import os

from userena.models import UserenaBaseProfile

import datetime
import os


GENDERS = (("M", "Male"), ("F", "Female"))
PROFILE_IMAGE_PATH = os.path.join('images','facebook_profiles/%Y/%m/%d')

class Profile(UserenaBaseProfile):
    user = models.OneToOneField(User,
        unique=True, verbose_name=_('User'), related_name='profile')
    birth_date = models.DateField(_('Birth date'), blank=True, null=True)
    gender = models.CharField(choices=GENDERS, max_length=63,
        blank=True, null=True, )
    about = models.TextField(_('About'), blank=True)
    ## TIME STAMPERS
    date_joined = models.DateTimeField(verbose_name=_("Date joined"),
        default=now)
    last_updated = models.DateTimeField(verbose_name=_("Last updated"),
        default=now)
    date_of_birth = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_joined = now()
        self.last_updated = now()

        super(Profile, self).save(*args, **kwargs)

    def __unicode__(self):
        return "Profile of {}".format(self.user.__unicode__())

    @models.permalink
    def get_absolute_url(self):
        return ('userena_profile_detail', [self.user.username,])

    @property
    def age(self):
        if not self.birth_date:
            return False
        else:
            today = datetime.date.today()
            try:
                birthday = self.birth_date.replace(year=today.year)
            except ValueError:
                day = today.day - 1 if today.day != 1 else today.day + 2
                birthday = self.birth_date.replace(year=today.year, day=day)

            if birthday > today:
                return today.year - self.birth_date.year - 1
            else:
                return today.year - self.birth_date.year
