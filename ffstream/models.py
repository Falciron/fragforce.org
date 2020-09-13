from django.db import models
import uuid
from django.conf import settings


class Key(models.Model):
    id = models.CharField(max_length=255, primary_key=True, blank=True)
    name = models.SlugField(max_length=256, unique=True)
    # owner = models.ForeignKey('ffsfdc.Contact', on_delete=models.CASCADE, null=False, blank=False)
    created = models.DateTimeField(verbose_name="Created At", null=True, blank=True, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True, blank=True, verbose_name="Modified At")
    is_live = models.BooleanField(null=False, default=False, blank=True, verbose_name="Is Live")
    active = models.BooleanField(default=True, blank=True, verbose_name="Can be used for streaming")
    pull = models.BooleanField(default=False, blank=True, verbose_name="Can be used for pulling streaming")

    def __str__(self):
        return self.name

class Stream(models.Model):
    guid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    key = models.ForeignKey(Key, on_delete=models.CASCADE, null=False, blank=False)
    # owner = models.ForeignKey('ffsfdc.Contact', on_delete=models.CASCADE, null=False, blank=False)
    created = models.DateTimeField(verbose_name="Created At", auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True, verbose_name="Modified At")
    is_live = models.BooleanField(null=False, default=False, verbose_name="Is Live")
    started = models.DateTimeField(verbose_name="Started Streaming At", null=True)
    ended = models.DateTimeField(verbose_name="Ended Streaming At", null=True)

    def url(self):
        return "%s/dash/%s__%s/index.mpd" % (
            settings.STREAM_DASH_BASE,
            self.key.name,
            self.guid,
        )

    def __str__(self):
        return "%s__%s" % (self.key.name, self.guid)
