from django.db import models
from community.models import Community


class Content(models.Model):
    url = models.URLField(unique=True)
    domain = models.CharField(max_length=240, blank=True)

    title = models.CharField(max_length=240, blank=True)
    excerpt = models.TextField(blank=True)
    content = models.TextField(blank=True)
    lead_image_url = models.URLField(blank=True, null=True)

    community = models.ManyToManyField(Community, related_name='content')

    date_published = models.DateTimeField(blank=True, null=True)
    word_count = models.IntegerField(blank=True, null=True)
    view_count = models.IntegerField(blank=True, null=True)
    share_count = models.IntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __unicode__(self):
        return self.url
