from django.db import models
from django.urls import reverse
from newsportalapp.utils import unique_slug_generator
from django.db.models.signals import pre_save


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class Tech_News(models.Model):
    headline = models.CharField(max_length=255)
    reporter = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()
    picture1 = models.ImageField(upload_to=upload_location, blank=True, null=True)
    picture2 = models.ImageField(upload_to=upload_location, blank=True, null=True)
    picture3 = models.ImageField(upload_to=upload_location, blank=True, null=True)
    thumbnail = models.ImageField(upload_to=upload_location, blank=True, null=True)
    published_at = models.DateTimeField(auto_now=True)
    event_place = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(allow_unicode=True, unique=True, blank=True, null=True)

    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse("tech:all", kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.id


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
        if not instance.slug:
            instance.slug = unique_slug_generator(instance)


pre_save.connect(rl_pre_save_receiver, sender=Tech_News)
