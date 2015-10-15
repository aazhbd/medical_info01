# -*- coding: utf-8 -*-

import hashlib
from random import random

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from irpmemr.models import CommonModel


TELE_STATUS_CHOICES = (
    ('NO', 'UNSUCCESS'),
    ('SU', 'SUCCESS'),
    ('DC', 'DISCONNECTED'),
    ('CA', 'CALLING'),
    ('FI', 'FINISH'),
)

class TeleconsultationManager(models.Manager):
    """
    manager class for Teleconsultation
    """
    def generate_unique_key(self, specialist, midwife):
        """
        generate Teleconsultation unique key to connect
        first check if the Teleconsultation unique key already exist
        """
        ps_ky = ''
        while not ps_ky:
            salt = hashlib.sha1(str(random())).hexdigest()[:5]
            unique_key = hashlib.sha1(salt + specialist.username + midwife.username).hexdigest()[:10]

            try:
                tele = self.model.objects.get(ps_ky=unique_key)
            except:
                tele = self.model(
                    specialist = specialist,
                    midwife = midwife,
                    ps_ky = unique_key,
                )
                tele.save()
                ps_ky = unique_key
        return unique_key

class Teleconsultation(CommonModel):
    """
    Store consultation record between specialist and midwife
    """
    specialist = models.ForeignKey(User, related_name="tele_specialists")
    midwife = models.ForeignKey(User, related_name="tele_midwives")
    ps_ky = models.CharField(max_length=100, blank=True, help_text="special key to connect")
    duration = models.CharField(max_length=10)
    status = models.CharField(max_length=2, choices=TELE_STATUS_CHOICES, default='NO')
    details = models.TextField(blank=True)

    objects = TeleconsultationManager()

    def __unicode__(self):
        return "%s : %s" % (str(self.specialist), str(self.midwife))

    def get_absolute_url(self):
        return reverse('teleconsultation', kwargs={'ps_ky':self.ps_ky})

