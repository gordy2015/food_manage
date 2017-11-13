# food_manage
first django project 2017-09-18

一个关于点餐的简单后台管理系统（第一版，练手，持续更新，待完善...）

数据库
python manage.py makemigrations
python manage.py migrate

公司 c
家   h
------------------------------------------
更新日志
2017-11-13 18:30 (c)
现有bug: 添加订单， 可以增加菜品数量，但无法添加新菜品

2017-11-13 23：53
修复：修改表结构， 其中表food_choose增加table_n字段做唯一识别(与table_manage的id一致)；
     添加订单模块已可以使用(增加菜品的数量与添加新菜品都正常)。 未计算all_price
