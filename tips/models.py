from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tip(models.Model):
	title = models.CharField(max_length=255)
	body = models.TextField()
	created_at = models.DateTimeField()

	def __str__(self):
		return self.title