import math
print(math.floor(1.2)) #
print(math.ceil(2.1)) #올림
print(math.floor(1.9)) #내림

from math import sin, cos, tan, ceil, floor
print(sin(1))
print(cos(1))
print(ceil(2.1))

import random as r
print(r.randrange(0,10))
a=[1,2,3,4,5]
print(r.sample(a,k=3))

import datetime as d
print(d.datetime.now().year)

from urllib import request
a=request.urlopen('https://google.com')
b=a.read()
print(b)