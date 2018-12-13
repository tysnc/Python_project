# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#这是一个自动生成的Django模型模块。
#您必须手动执行以下操作来清理：
#*重新排列模型的顺序
#*确保每个模型都有一个包含._key=True的字段
#*确保每个ForeignKey都已将“on_delete”设置为所需的行为。
#*如果希望允许Django创建、修改和删除表，请删除`managed=False'行
#可以随意重命名模型，但不要重命名db_table值或字段名。


from django.db import models
class Tbdept(models.Model):
    dno = models.IntegerField(primary_key=True)
    dname = models.CharField(unique=True, max_length=10)
    dloc = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'TbDept'


class Tbemp(models.Model):
    eno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=20)
    job = models.CharField(max_length=20)
    mgr = models.IntegerField(blank=True, null=True)
    sal = models.IntegerField()
    comm = models.IntegerField(blank=True, null=True)
    dno = models.ForeignKey(Tbdept, models.DO_NOTHING, db_column='dno', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TbEmp'
