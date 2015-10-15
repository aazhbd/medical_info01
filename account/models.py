# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse

from irpmemr.models import CommonModel



ACCESS_CHOICES = (
    ('AD', 'Admin'),
    ('SP', 'Specialist'),
    ('MW', 'Midwife'),
    ('NO', 'Normal'),
)

class UserProfile(CommonModel):
    user = models.OneToOneField(User, unique=True)
    access_type = models.CharField(max_length=2, choices=ACCESS_CHOICES, default='NO')
    skype_id = models.CharField(max_length=32, blank=True)
    phone_number = models.CharField(max_length=32, blank=True)
    remarks = models.TextField(blank=True)

    def __unicode__(self):
        return self.user.username

    def check_user_type(self):
        """
        check user type, midwife or specialist
        """
        # self.user.
        return

class Messages(CommonModel):
    sender = models.ForeignKey(User, related_name='sender')
    receiver = models.ForeignKey(User, related_name='receiver')
    msgbody = models.CharField(max_length=500)
    submitted_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.sender)


STATUS_CHOICES = (
    ('BU', "Busy"),
    ('AW', "Away"),
    ('AV', "Available"),
    ('OF', "Offline"),
    ('OC', "On call"),
)

class Specialist(CommonModel):
    user = models.OneToOneField(User)
    information = models.TextField(blank=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default="OF")
    rate = models.DecimalField(max_digits=11, decimal_places=2, default='0')
    details = models.TextField(blank=True)

    def __unicode__(self):
        return self.user.get_full_name()

    def view_rate(self):
        """
        return rate view
        """
        return "RM %s/session" % self.rate

    def get_absolute_url(self):
        return reverse('specialist_view', kwargs={'specialist_id':self.user.id})

    def available(self):
        """
        check if specialist is available
        """
        if self.status in ["AV", "AW",]:
            return True
        else:
            return False

#### POST SAVE USER ####
def update_user_access(sender, instance, **kwargs):
    """
    Update user access in UserProfile model
    If no UserProfile, it will be created first
    then user access will be assigned
    Admin, Midwife, Specialist can only be created from admin site
    set the group either for midwife or specialist
    For admin, just set is staff to True
    """
    try:
        user = instance
        user_profile = UserProfile.objects.get_or_create(user=user)[0]
        if user.is_superuser or user.is_staff:
            # admin or superuser
            # set access to AD
            user_profile.access_type = 'AD'
        elif user.groups.filter(name="Midwife"):
            # midwife set access to MW
            user_profile.access_type = 'MW'
        elif user.groups.filter(name="Specialist"):
            # create an entry in Specialist model
            sp = Specialist.objects.get_or_create(user=user)[0]

            # specialist set access to SP
            user_profile.access_type = 'SP'
        user_profile.save()
    except Exception, e:
        print e
        pass

post_save.connect(update_user_access, sender=User)
