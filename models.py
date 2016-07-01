# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    """用户信息，包括private_token等属性
    """
    user = models.OneToOneField(User)
    private_token = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.user.username
