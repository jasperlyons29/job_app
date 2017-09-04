# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import (
	Model,
	TextField
)


# Create your models here.
class JobListing(Model):
	title = TextField(null=True, blank=True)
	description = TextField(null=True, blank=True)