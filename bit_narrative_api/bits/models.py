from django.db import models

from accounts.models import Account
from content.models import Content


class Bit(models.Model):
    bit = models.CharField(max_length=240)
    content_index = models.IntegerField()

    content = models.ForeignKey(Content, related_name='bits')
    accounts = models.ManyToManyField(Account, related_name='bits')

    view_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)
    up_count = models.IntegerField(default=0)
    down_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        unique_together = ('content', 'content_index', )

    def __unicode__(self):
        return self.bit
