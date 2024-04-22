
from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group


class Images(models.Model):
    original_filename = models.CharField(max_length=2000, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    universal_url = models.CharField(max_length=500, blank=True, null=True)
    original_path = models.CharField(max_length=2000, blank=True, null=True)
    redacted = models.IntegerField(blank=True, null=True)
    internal_filename = models.CharField(max_length=500, blank=True, null=True)
    notes = models.CharField(max_length=8192, blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    collection = models.CharField(max_length=50, blank=True, null=True)
    orig_md5 = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'images'

# class UserProfile(AbstractUser):
#     password = models.CharField(max_length=200, blank=True, null=True)
#
#     class Meta:
#         using = "default"
#         managed = True
#         db_table = 'auth_user'


# class Role(models.Model):
#     name = models.CharField(max_length=255)
#     permissions = models.ManyToManyField(Permission, related_name='roles')
#     class Meta:
#         managed = True
#         db_table = 'auth_user'
#         using = 'default'


