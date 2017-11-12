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

class foodtype_manage(models.Model):
    foodtypename = models.CharField(max_length=32)


class food_manage(models.Model):
    foodname = models.CharField(max_length=16)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    vip_price = models.DecimalField(max_digits=12, decimal_places=2)
    foodtype = models.ForeignKey(to='foodtype_manage',to_field='id')



class order(models.Model):
    table = models.ForeignKey(to='table_manage',to_field='id')
    order_s = models.ForeignKey(to='table_status', to_field='id')
    # all_price = models.FloatField(max_length=12)
    # order_de = models.ManyToManyField(order_detail)

# class orderstatus(models.Model):
#     orderstatus = models.CharField(max_length=12)

class food_choose(models.Model):
    food_count = models.CharField(max_length=12,default=1)
    food_cho = models.ForeignKey(to='food_manage', to_field='id')


class order_detail(models.Model):
    thisorder = models.ForeignKey(to='order',to_field='id')
    thisfc = models.ForeignKey(to='food_choose',to_field='id')









