# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class BaseModel(models.Model):
    created_by = models.ForeignKey(User)
    created_date = models.DateTimeField()
    last_update_by = models.ForeignKey(User)
    last_update_date = models.DateTimeField()

    class Meta:
            abstract = True
