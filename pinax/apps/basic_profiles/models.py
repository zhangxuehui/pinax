from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User



class Profile(models.Model):
    
    user = models.ForeignKey(User, unique=True, verbose_name=_("user"))
    name = models.CharField(_("name"), max_length=50, null=True, blank=True)
    about = models.TextField(_("about"), null=True, blank=True)
    location = models.CharField(_("location"), max_length=40, null=True, blank=True)
    website = models.URLField(_("website"), null=True, blank=True, verify_exists=False)
    
    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")
    
    def __unicode__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"username": self.user.username})


def create_profile(sender, instance=None, **kwargs):
    if instance is None:
        return
    profile, created = Profile.objects.get_or_create(user=instance)


post_save.connect(create_profile, sender=User)
