# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TbAgent(models.Model):
    agentid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    tel = models.CharField(max_length=20)
    servstar = models.IntegerField()
    realstar = models.IntegerField()
    profstar = models.IntegerField()
    certificated = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tb_agent'


class TbAgentEstate(models.Model):
    agent_estate_id = models.AutoField(primary_key=True)
    agentid = models.ForeignKey(TbAgent, models.DO_NOTHING, db_column='agentid')
    estateid = models.ForeignKey('TbEstate', models.DO_NOTHING, db_column='estateid')

    class Meta:
        managed = False
        db_table = 'tb_agent_estate'
        unique_together = (('agentid', 'estateid'),)


class TbDistrict(models.Model):
    distid = models.IntegerField(primary_key=True)
    pid = models.ForeignKey('self', models.DO_NOTHING, db_column='pid', blank=True, null=True)
    name = models.CharField(max_length=255)
    intro = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_district'


class TbEstate(models.Model):
    estateid = models.AutoField(primary_key=True)
    distid = models.ForeignKey(TbDistrict, models.DO_NOTHING, db_column='distid')
    name = models.CharField(max_length=255)
    hot = models.IntegerField(blank=True, null=True)
    intro = models.CharField(max_length=511, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_estate'


class TbHouseInfo(models.Model):
    houseid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    area = models.IntegerField()
    floor = models.IntegerField()
    totalfloor = models.IntegerField()
    direction = models.CharField(max_length=10)
    price = models.IntegerField()
    priceunit = models.CharField(max_length=10)
    detail = models.CharField(max_length=511, blank=True, null=True)
    mainphoto = models.CharField(max_length=255)
    pubdate = models.DateTimeField()
    street = models.CharField(max_length=255)
    hassubway = models.IntegerField()
    isshared = models.IntegerField()
    hasagentfees = models.IntegerField()
    typeid = models.ForeignKey('TbHouseType', models.DO_NOTHING, db_column='typeid')
    userid = models.ForeignKey('TbUser', models.DO_NOTHING, db_column='userid')
    distid = models.ForeignKey(TbDistrict, models.DO_NOTHING, db_column='distid')
    estateid = models.ForeignKey(TbEstate, models.DO_NOTHING, db_column='estateid', blank=True, null=True)
    agentid = models.ForeignKey(TbAgent, models.DO_NOTHING, db_column='agentid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_house_info'


class TbHousePhoto(models.Model):
    photoid = models.AutoField(primary_key=True)
    houseid = models.ForeignKey(TbHouseInfo, models.DO_NOTHING, db_column='houseid')
    path = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tb_house_photo'


class TbHouseTag(models.Model):
    house_tag_id = models.AutoField(primary_key=True)
    houseid = models.ForeignKey(TbHouseInfo, models.DO_NOTHING, db_column='houseid')
    tagid = models.ForeignKey('TbTag', models.DO_NOTHING, db_column='tagid')

    class Meta:
        managed = False
        db_table = 'tb_house_tag'
        unique_together = (('houseid', 'tagid'),)


class TbHouseType(models.Model):
    typeid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tb_house_type'


class TbLoginLog(models.Model):
    logid = models.BigAutoField(primary_key=True)
    userid = models.ForeignKey('TbUser', models.DO_NOTHING, db_column='userid')
    ipaddr = models.CharField(max_length=255)
    logdate = models.DateTimeField()
    devcode = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tb_login_log'


class TbRecord(models.Model):
    recordid = models.BigAutoField(primary_key=True)
    userid = models.ForeignKey('TbUser', models.DO_NOTHING, db_column='userid')
    houseid = models.ForeignKey(TbHouseInfo, models.DO_NOTHING, db_column='houseid')
    recorddate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_record'
        unique_together = (('userid', 'houseid'),)


class TbTag(models.Model):
    tagid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tb_tag'


class TbUser(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=32)
    realname = models.CharField(max_length=20)
    tel = models.CharField(unique=True, max_length=20)
    email = models.CharField(unique=True, max_length=255)
    createdate = models.DateTimeField()
    point = models.IntegerField()
    isagent = models.IntegerField()
    lastvisit = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_user'


class TbUserToken(models.Model):
    tokenid = models.AutoField(primary_key=True)
    token = models.CharField(max_length=32)
    userid = models.ForeignKey(TbUser, models.DO_NOTHING, db_column='userid', unique=True)

    class Meta:
        managed = False
        db_table = 'tb_user_token'
