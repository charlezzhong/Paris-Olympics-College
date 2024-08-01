# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Athlete(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    country_team = models.CharField(max_length=50, blank=True, null=True)
    olympic_role = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'athletes'
        ordering = ['id']

class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    conference = models.CharField(max_length=255)
    division = models.CharField(max_length=50)

    class Meta:
        db_table = 'schools'
        ordering = ['id']

class Sport(models.Model):
    id = models.AutoField(primary_key=True)
    ncaa_sport = models.CharField(max_length=255)
    olympic_sport = models.CharField(max_length=255)

    class Meta:
        db_table = 'sports'
        unique_together = (('ncaa_sport', 'olympic_sport'),)
        ordering = ['id']

class AthleteSchool(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    class Meta:
        db_table = 'athlete_school'
        unique_together = (('athlete', 'school'),)
        ordering = ['athlete', 'school']

class AthleteSport(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

    class Meta:
        db_table = 'athlete_sport'
        unique_together = (('athlete', 'sport'),)
        ordering = ['athlete', 'sport']