# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Arule(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    rules = models.TextField(db_column='Rules', blank=True, null=True)  # Field name made lowercase.
    support = models.TextField(db_column='Support', blank=True, null=True)  # Field name made lowercase.
    confidence = models.TextField(db_column='Confidence', blank=True, null=True)  # Field name made lowercase.
    lift = models.TextField(db_column='Lift', blank=True, null=True)  # Field name made lowercase.
    target = models.TextField(db_column='Target', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Arule'


class Customeremotion(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    emotion = models.TextField(db_column='Emotion', blank=True, null=True)  # Field name made lowercase.
    count = models.TextField(db_column='Count', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    per = models.TextField(db_column='PER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CustomerEmotion'


class Customeremotionall(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    overall = models.TextField(blank=True, null=True)
    anger = models.TextField(blank=True, null=True)  # This field type is a guess.
    anticipation = models.TextField(blank=True, null=True)  # This field type is a guess.
    disgust = models.TextField(blank=True, null=True)  # This field type is a guess.
    fear = models.TextField(blank=True, null=True)  # This field type is a guess.
    joy = models.TextField(blank=True, null=True)  # This field type is a guess.
    sadness = models.TextField(blank=True, null=True)  # This field type is a guess.
    surprise = models.TextField(blank=True, null=True)  # This field type is a guess.
    trust = models.TextField(blank=True, null=True)  # This field type is a guess.
    negative = models.TextField(blank=True, null=True)  # This field type is a guess.
    positive = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'CustomerEmotionAll'


class Sentimentsdata(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    sub_re = models.TextField(db_column='SUB_RE', blank=True, null=True)  # Field name made lowercase.
    sub_nre = models.TextField(db_column='SUB_NRE', blank=True, null=True)  # Field name made lowercase.
    re_txt = models.TextField(db_column='RE_TXT', blank=True, null=True)  # Field name made lowercase.
    org_txt = models.TextField(db_column='ORG_TXT', blank=True, null=True)  # Field name made lowercase.
    nre_txt = models.TextField(db_column='NRE_TXT', blank=True, null=True)  # Field name made lowercase.
    frm_email = models.TextField(db_column='FRM_EMAIL', blank=True, null=True)  # Field name made lowercase.
    to_email = models.TextField(db_column='TO_EMAIL', blank=True, null=True)  # Field name made lowercase.
    snd_day = models.TextField(db_column='SND_DAY', blank=True, null=True)  # Field name made lowercase.
    snd_date = models.TextField(db_column='SND_DATE', blank=True, null=True)  # Field name made lowercase.
    snd_time = models.TextField(db_column='SND_TIME', blank=True, null=True)  # Field name made lowercase.
    re_date = models.TextField(db_column='RE_DATE', blank=True, null=True)  # Field name made lowercase.
    re_day = models.TextField(db_column='RE_DAY', blank=True, null=True)  # Field name made lowercase.
    re_time = models.TextField(db_column='RE_TIME', blank=True, null=True)  # Field name made lowercase.
    nre_date = models.TextField(db_column='NRE_DATE', blank=True, null=True)  # Field name made lowercase.
    nre_day = models.TextField(db_column='NRE_DAY', blank=True, null=True)  # Field name made lowercase.
    nre_time = models.TextField(db_column='NRE_TIME', blank=True, null=True)  # Field name made lowercase.
    cust_email = models.TextField(db_column='CUST_EMAIL', blank=True, null=True)  # Field name made lowercase.
    vadr_score_pos_cust = models.TextField(db_column='VADR_SCORE_POS_CUST', blank=True, null=True)  # Field name made lowercase.
    vadr_score_neg_cust = models.TextField(db_column='VADR_SCORE_NEG_CUST', blank=True, null=True)  # Field name made lowercase.
    vadr_score_neu_cust = models.TextField(db_column='VADR_SCORE_NEU_CUST', blank=True, null=True)  # Field name made lowercase.
    vadr_score_com_cust = models.TextField(db_column='VADR_SCORE_COM_CUST', blank=True, null=True)  # Field name made lowercase.
    vadr_score_pos_supt = models.TextField(db_column='VADR_SCORE_POS_SUPT', blank=True, null=True)  # Field name made lowercase.
    vadr_score_neg_supt = models.TextField(db_column='VADR_SCORE_NEG_SUPT', blank=True, null=True)  # Field name made lowercase.
    vadr_score_neu_supt = models.TextField(db_column='VADR_SCORE_NEU_SUPT', blank=True, null=True)  # Field name made lowercase.
    vadr_score_com_supt = models.TextField(db_column='VADR_SCORE_COM_SUPT', blank=True, null=True)  # Field name made lowercase.
    punch_removed_cust = models.TextField(db_column='PUNCH_REMOVED_CUST', blank=True, null=True)  # Field name made lowercase.
    punch_removed_supt = models.TextField(db_column='PUNCH_REMOVED_SUPT', blank=True, null=True)  # Field name made lowercase.
    word_tokenized_cust = models.TextField(db_column='WORD_TOKENIZED_CUST', blank=True, null=True)  # Field name made lowercase.
    word_tokenized_supt = models.TextField(db_column='WORD_TOKENIZED_SUPT', blank=True, null=True)  # Field name made lowercase.
    summ_cust = models.TextField(db_column='SUMM_CUST', blank=True, null=True)  # Field name made lowercase.
    summ_supt = models.TextField(db_column='SUMM_SUPT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SentimentsData'


class Supportemotion(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    emotion = models.TextField(db_column='Emotion', blank=True, null=True)  # Field name made lowercase.
    count = models.TextField(db_column='Count', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    per = models.TextField(db_column='PER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SupportEmotion'


class Supportemotionall(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    overall = models.TextField(blank=True, null=True)
    anger = models.TextField(blank=True, null=True)  # This field type is a guess.
    anticipation = models.TextField(blank=True, null=True)  # This field type is a guess.
    disgust = models.TextField(blank=True, null=True)  # This field type is a guess.
    fear = models.TextField(blank=True, null=True)  # This field type is a guess.
    joy = models.TextField(blank=True, null=True)  # This field type is a guess.
    sadness = models.TextField(blank=True, null=True)  # This field type is a guess.
    surprise = models.TextField(blank=True, null=True)  # This field type is a guess.
    trust = models.TextField(blank=True, null=True)  # This field type is a guess.
    negative = models.TextField(blank=True, null=True)  # This field type is a guess.
    positive = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'SupportEmotionAll'


class Textsummaryd(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    summ_cust = models.TextField(db_column='SUMM_CUST', blank=True, null=True)  # Field name made lowercase.
    summ_supt = models.TextField(db_column='SUMM_SUPT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TextSummaryD'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BlogClean(models.Model):
    user = models.TextField()
    column_number = models.TextField()

    class Meta:
        managed = False
        db_table = 'blog_clean'


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField()
    author = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog_post'


class BlogTextdata(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)
    textfile = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'blog_textdata'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class UsersProfile(models.Model):
    image = models.CharField(max_length=100)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'users_profile'
