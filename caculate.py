# coding=utf-8
import math

print 2 + 5
print 4.0 + 2
print 4.00 + 2.00
print type(4.00)
print type(4)

print abs(-4)

print any([0, 1])
print any([0, 0])
print all([0, 1])
print all([1, 1])
print round(4.6)
print math.floor(4.3)
print math.sqrt(4)

# 除法
print 2 / 5
print 2.0 / 5

print round(3.1415, 2)

print 0 / 2 + 0 / 4 + 1 / 8.0

# 商和余数
print divmod(5, 2)

print round(1.234567, 3)
print round(1.2345, 3)


def show(x):
    print '{:.20f}'.format(x)


show(1.234567)
show(1.2345)
