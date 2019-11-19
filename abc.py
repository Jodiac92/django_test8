# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models                                                          # python manage.py inspectdb > abc.py** 중요


class Admin(models.Model):
    admin_id = models.CharField(primary_key=True, max_length=20)
    admin_passwd = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'admin'


class Board(models.Model):
    num = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    pass_field = models.CharField(db_column='pass', max_length=20)  # Field renamed because it was a Python reserved word.
    mail = models.CharField(max_length=30, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    cont = models.TextField(blank=True, null=True)
    bip = models.CharField(max_length=20, blank=True, null=True)
    bdate = models.CharField(max_length=20, blank=True, null=True)
    readcnt = models.IntegerField(blank=True, null=True)
    gnum = models.IntegerField(blank=True, null=True)
    onum = models.IntegerField(blank=True, null=True)
    nested = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'board'


class Buser(models.Model):
    buser_no = models.IntegerField(primary_key=True)
    buser_name = models.CharField(max_length=10)
    buser_loc = models.CharField(max_length=10, blank=True, null=True)
    buser_tel = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buser'


class Gogek(models.Model):
    gogek_no = models.IntegerField(primary_key=True)
    gogek_name = models.CharField(max_length=10)
    gogek_tel = models.CharField(max_length=20, blank=True, null=True)
    gogek_jumin = models.CharField(max_length=14, blank=True, null=True)
    gogek_damsano = models.ForeignKey('Jikwon', models.DO_NOTHING, db_column='gogek_damsano', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gogek'


class Gogek2(models.Model):
    userid = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=10)
    zipcode = models.CharField(max_length=7)
    area1 = models.CharField(max_length=10)
    area2 = models.CharField(max_length=20)
    area3 = models.CharField(max_length=30)
    area4 = models.CharField(max_length=50)
    tel = models.CharField(max_length=15, blank=True, null=True)
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    location = models.CharField(max_length=10, blank=True, null=True)
    purpose = models.CharField(max_length=10, blank=True, null=True)
    regdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gogek2'


class Jikwon(models.Model):
    jikwon_no = models.IntegerField(primary_key=True)
    jikwon_name = models.CharField(max_length=10)
    buser_num = models.IntegerField()
    jikwon_jik = models.CharField(max_length=10, blank=True, null=True)
    jikwon_pay = models.IntegerField(blank=True, null=True)
    jikwon_ibsail = models.DateField(blank=True, null=True)
    jikwon_gen = models.CharField(max_length=4, blank=True, null=True)
    jikwon_rating = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jikwon'


class Member(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    passwd = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    zipcode = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    job = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member'


class Membertab(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=10)
    passwd = models.CharField(max_length=10)
    reg_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'membertab'


class Sangdata(models.Model):
    code = models.IntegerField(primary_key=True)
    sang = models.CharField(max_length=20, blank=True, null=True)
    su = models.IntegerField(blank=True, null=True)
    dan = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sangdata'


class ShopOrder(models.Model):
    no = models.AutoField(primary_key=True)
    product_no = models.CharField(max_length=5)
    quantity = models.CharField(max_length=10, blank=True, null=True)
    sdate = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=10, blank=True, null=True)
    id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_order'


class ShopProduct(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    price = models.CharField(max_length=10, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    sdate = models.DateTimeField(blank=True, null=True)
    stock = models.CharField(max_length=10, blank=True, null=True)
    image = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_product'


class Userinfo(models.Model):
    userid = models.CharField(primary_key=True, max_length=10)
    password = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userinfo'


class Ziptab(models.Model):
    zipcode = models.CharField(max_length=7, blank=True, null=True)
    area1 = models.CharField(max_length=10, blank=True, null=True)
    area2 = models.CharField(max_length=20, blank=True, null=True)
    area3 = models.CharField(max_length=30, blank=True, null=True)
    area4 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ziptab'
