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


class Category(models.Model):
    caption = models.CharField(max_length=32)

class ArticleType(models.Model):
    caption = models.CharField(max_length=32)

class Article(models.Model):
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    article_type = models.ForeignKey(ArticleType)



class foodtype_manage(models.Model):
    foodtypename = models.CharField(max_length=32)

class food_manage(models.Model):
    foodname = models.CharField(max_length=32)
    price = models.FloatField(max_length=12)
    vip_price = models.FloatField(max_length=12)
    foodtype = models.ForeignKey(to='foodtype_manage',to_field='id')

class order(models.Model):
    tablename = models.ForeignKey(to='table_manage',to_field='id')
    all_price = models.FloatField(max_length=12)
    orderstatus = models.CharField(max_length=12)





