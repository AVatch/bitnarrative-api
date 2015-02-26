from django.db import models

from accounts.models import Account
from content.models import Content


class Bit(models.Model):
    bit = models.CharField(max_length=240)
    content_index = models.IntegerField()

    content = models.ForeignKey(Content, related_name='bits')
    accounts = models.ManyToManyField(Account, related_name='bits')

    view_count = models.IntegerField(blank=True, null=True)
    share_count = models.IntegerField(blank=True, null=True)
    up_count = models.IntegerField(blank=True, null=True)
    down_count = models.IntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
        unique_together = ('content', 'content_index', )
