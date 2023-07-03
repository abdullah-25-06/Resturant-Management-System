# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class MenuOrder(models.Model):
    o_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')
    item_price = models.IntegerField()
    id = models.ForeignKey(User, models.DO_NOTHING, db_column='id', blank=True, null=True)
    ordertime = models.TimeField(db_column='OrderTime', blank=True, null=True)  # Field name made lowercase.
    orderdate = models.DateField(db_column='OrderDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'menu_order'
