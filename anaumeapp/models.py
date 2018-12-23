# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class FillquestionDetail(models.Model):
    fillquestion_detail_id = models.AutoField(primary_key=True)
    fillquestion = models.OneToOneField('Fillquestions', models.DO_NOTHING)
    text = models.CharField(max_length=255)
    answer_text = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'fillquestion_detail'


class Fillquestions(models.Model):
    fillquestion_id = models.AutoField(primary_key=True)
    original_text = models.OneToOneField('OriginalTexts', models.DO_NOTHING)
    fillquestion_name = models.CharField(max_length=255)
    registed_on = models.DateTimeField()
    regist_user = models.IntegerField()
    updated_on = models.DateTimeField()
    update_user = models.IntegerField()

    class Meta:
        db_table = 'fillquestions'


class OriginalTexts(models.Model):
    original_text_id = models.AutoField(primary_key=True)
    original_text = models.TextField()
    registed_on = models.DateTimeField()
    regist_user = models.IntegerField()
    updated_on = models.DateTimeField()
    update_user = models.IntegerField()

    class Meta:
        db_table = 'original_texts'
