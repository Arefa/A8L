# -*-coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    telphone = models.CharField(max_length=11)

    def __unicode__(self):
        return self.user.username


class Form(models.Model):
    form_id = models.UUIDField()
    form_name = models.CharField(max_length=128, default='未命名表单')
    create_time = models.DateTimeField()
    edit_time = models.DateTimeField()
    create_person = models.ForeignKey(User)
    cooperation = models.BinaryField(default=0)
    # cooperate_person = models.ForeignKey(User)
    fill_mode = models.BinaryField(default=0)
    # fill_person = models.ForeignKey(User)

    def __unicode__(self):
        return self.form_name









