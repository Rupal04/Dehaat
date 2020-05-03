# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class BalSheet(models.Model):
    class Meta(object):
        db_table = 'balsheet'
    particular = models.CharField(max_length=800, blank=False, null=False)
    year_2015 = models.CharField(max_length=200)
    year_2016 = models.CharField(max_length=200)
