
from django import template
from django.utils.safestring import mark_safe
import time

register = template.Library()

@register.simple_tag
def singlefee(v1,v2):
    m = int(v1) * int(v2)
    m = ("%.2f" % m)
    ret = '%s' % m
    return mark_safe(ret)


import ast  #用于把str类型转成float
def allfee(v1):
    m = float(0)
    for i in v1.split(' '):
        if i.strip():
            t = ast.literal_eval(i)
            # print(type(t))
            m = m + t
    print(m)

# allfee(' 68.0 69.0 18.0 70.0 14.0')


# @register.filter
# def jiajingze(a1,a2):
#     print(a2,type(a2))
#     return a1 + str(a2)

def normaltime(v1):
    t = time.strftime("%Y-%m-%d %H:%M:%S", v1)
    print(t)