# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
