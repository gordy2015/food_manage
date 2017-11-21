# food_manage
first django project build in 2017-09-18

一个关于点餐的简单后台管理系统（第一版，练手，持续更新，待完善...）

数据库
python manage.py makemigrations
python manage.py migrate

公司 c
家   h

[更新日志]
------------------------------------------
[v0.1]
idea诞生--》 初版
2017-11-13 18:30 (c)
现有bug: 添加订单， 可以增加菜品数量，但无法添加新菜品

2017-11-13 23：53 (h)
修复：修改表结构， 其中表food_choose增加table_n字段做唯一识别(与table_manage的id一致)；
     添加订单模块已可以使用(增加菜品的数量与添加新菜品都正常)。 未计算all_price

2017-11-14 18:00 (c)
增加：someFunce为 all_price计算函数（动态变化）
     订单分成未结账订单和历史订单，增加订单删除/订单结算/订单详情中单菜品删除的功能

2017-11-14 21:30 (h)
增加：可修改订单详情的菜品数量

2017-11-14 22:47 (h)
增加: 餐桌属于普通会员或高级会员（是否VIP对单价有区别）

----------------------------------------
[v0.2]
重新设计数据库表的结构和功能逻辑
2017-11-15 18:08 (c)
修复: 增加用户组/菜系 改用ajax ，对其输入的值做限制（不能为空）
      修改订单相关的表的结构，VIP、下单时间移到order表，并修改订单基于订单号，而不再基于餐桌（ablename）
      ajax相关的函数中 ret = {'status': True, 'eror': None, 'data': None} 改成 ret = {'status': True, 'info': None, 'data': None}

2017-11-15 00:02(h)
增加: order增删查的功能完善，重新添加计算all_price

2017-11-19 00:57(h):
增加：完成以订单号为基准，一桌可下N个订单
    数据库表结构修改，order表与food_choose表以ou_id和order_n_id两个字段做关联。 下单时间默认是当前时间


2017-11-21 18:17 (c):
增加：使用官方bootstarp的CSS： 下载并解压后把css,js,fonts目录放入/static/目录
    
