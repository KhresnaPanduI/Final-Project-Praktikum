from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    masker_medis    = models.IntegerField(blank=True, null=True)
    masker_n95      = models.IntegerField(blank=True, null=True)
    hazmat          = models.IntegerField(blank=True, null=True)
    apron           = models.IntegerField(blank=True, null=True)
    hand_sanitizer  = models.IntegerField(blank=True, null=True)
    sarung_tangan   = models.IntegerField(blank=True, null=True)
    face_shield     = models.IntegerField(blank=True, null=True)
    sepatu_boots    = models.IntegerField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("akun:detail-apd", kwargs={"id": self.id})
