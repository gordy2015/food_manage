from django.db import models

# Create your models here.

class user_group(models.Model):
    groupname = models.CharField(max_length=12)

class user_info(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    grouptype = models.ForeignKey(to='user_group', to_field='id')

class table_status(models.Model):
    tablestatus = models.CharField(max_length=12)

class table_manage(models.Model):
    tablename = models.CharField(max_length=32)
    ordertime = models.CharField(max_length=32)
    ts = models.ForeignKey(to='table_status', to_field='id')
    tlevel = (
        (0, u'普通会员'),
        (1, u'VIP会员'),
    )
    tlevel_type = models.IntegerField(choices=tlevel)

class foodtype_manage(models.Model):
    foodtypename = models.CharField(max_length=32)


class food_manage(models.Model):
    foodname = models.CharField(max_length=16)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    vip_price = models.DecimalField(max_digits=12, decimal_places=2)
    foodtype = models.ForeignKey(to='foodtype_manage',to_field='id')



class order(models.Model):
    table = models.ForeignKey(to='table_manage',to_field='id')
    # order_s = models.ForeignKey(to='table_status', to_field='id')
    all_price = models.DecimalField(max_digits=12,decimal_places=2,default=0.00)
    # order_de = models.ManyToManyField(order_detail)


class food_choose(models.Model):
    food_count = models.CharField(max_length=12,default=1)
    food_cho = models.ForeignKey(to='food_manage', to_field='id')
    table_n = models.CharField(max_length=12,null=True)


class order_detail(models.Model):
    thisorder = models.ForeignKey(to='order',to_field='id')
    thisfc = models.ForeignKey(to='food_choose',to_field='id')









