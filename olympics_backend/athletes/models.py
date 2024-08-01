# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Ultitable(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    school = models.CharField(max_length=255)
    conference = models.CharField(max_length=255)
    division = models.CharField(max_length=10)
    ncaa_sport = models.CharField(max_length=255)
    olympic_sport = models.CharField(max_length=255)
    country_team = models.CharField(max_length=100)
    olympic_role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    class Meta:
        db_table = 'ultitable'  # Explicitly specify the table name