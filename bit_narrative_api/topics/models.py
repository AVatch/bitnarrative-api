from django.db import models

from accounts.models import Account
from community.models import Community
from content.models import Content


class Topic(models.Model):
    topic = models.CharField(max_length=240, blank=True)
    lead_image_url = models.URLField(blank=True, null=True)

    accounts = models.ManyToManyField(Account, related_name='topic')
    communities = models.ManyToManyField(Community, related_name='topic')
    content = models.ManyToManyField(Content, related_name='topic')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('topic',)

    def __unicode__(self):
        return self.topic
