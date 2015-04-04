from django.db import models

from accounts.models import Account
from topics.models import Topic


class Community(models.Model):
    community = models.CharField(max_length=200, blank=True)
    community_description = models.CharField(max_length=240, blank=True)
    lead_image_url = models.URLField(blank=True, null=True)

    accounts = models.ManyToManyField(Account, related_name='community')
    topics = models.ManyToManyField(Topic, related_name='community')

    participation_rate = models.FloatField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated_at',)

    def __unicode__(self):
        return self.community
