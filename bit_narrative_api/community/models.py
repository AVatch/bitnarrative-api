from django.db import models

from accounts.models import Account
# Create your models here.


class Community(models.Model):
    group_name = models.CharField(max_length=240, blank=True)
    lead_image_url = models.URLField(blank=True, null=True)
    member_count = models.IntegerField(blank=True, null=True)
    community_description = models.CharField(max_length=240, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    participation_rate = models.FloatField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    accounts = models.ManyToManyField(Account, related_name='community')

    class Meta:
        ordering = ('-member_count',)

    def __unicode__(self):
        return self.group_name
