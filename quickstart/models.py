# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Arule(models.Model):
    index = models.BigIntegerField(blank=True, null=True) #, primary_key=True)
    rules = models.CharField(db_column='Rules', blank=True, null=True,max_length = 100)  # Field name made lowercase.
    support = models.TextField(db_column='Support', blank=True, null=True)  # Field name made lowercase.
    confidence = models.TextField(db_column='Confidence', blank=True, null=True)  # Field name made lowercase.
    lift = models.TextField(db_column='Lift', blank=True, null=True)  # Field name made lowercase.
    target = models.CharField(db_column='Target', blank=True, null=True,max_length = 100)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'Arule'



class Customeremotion(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    emotion = models.TextField(db_column='Emotion', blank=True, null=True)  # Field name made lowercase.
    count = models.TextField(db_column='Count', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    per = models.TextField(db_column='PER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'CustomerEmotion'






