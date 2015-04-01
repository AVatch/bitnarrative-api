from django.db import models

from accounts.models import Account
from topics.models import Topic


class Community(models.Model):
    group_name = models.CharField(max_length=240, blank=True)
    lead_image_url = models.URLField(blank=True, null=True)
    community_description = models.CharField(max_length=240, blank=True)

    accounts = models.ManyToManyField(Account, related_name='community')
    topics = models.ForeignKey(Topic, related_name='community')

    member_count = models.IntegerField(blank=True, null=True)
    participation_rate = models.FloatField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-member_count',)

    def __unicode__(self):
        return self.group_name
