# def f(x):
#   return (x**2+2*x-1)

# def df1(x,h):
#   return ((f(x+h)-f(x))/h)

# def df2(x,h):
#   return ((f(x)-f(x-h))/h)

# def df3(x,h):
#   return ((f(x+h)-f(x-h))/(2*h))

# def df4(x,a):
#   return (f(x)-f(a))/(x-a)

# print('f(1)={:d},df(1)={:.4f}'.format(f(1),df1(1,0.01)))
# print('f(1)={:d},df(1)={:.4f}'.format(f(1),df2(1,0.01)))
# print('f(1)={:d},df(1)={:.4f}'.format(f(1),df3(1,0.01)))
# print('f(1)={:d},df(1)={:.4f}'.format(f(1),df4(1,0.999)))



def f(x):
  return (x**2-x*2+1)

def g(x):
  return (x**3+x*2)

def h(x):
  return (f(x)-g(x))

def dh(x,t):
  return (h(x+t)-h(x-t))/(2*t)


#=========================================
c=0.000000000001
t=0.000000000001
xi=3
count=0
while (abs(h(xi))>c):
  xf=xi-h(xi)/dh(xi,t)
  xi=xf
  count+=1
  print('count={},\txf={}'.format(count,xi))

print('====================================')
print('{}'.format(xf))



import 근 as r
r.root(xi,g,h,t,cri)






def f(x,g,h):
  return g(x)-h(x)

def df(x,g,h,t):
  return (f(x+t,g,h)-f(x-t,g,h))/2*t

def root(xi,g,h))>cri:
  count=0
  while (abs(f(xi,g,h))>cri):
    xf=xi-f(xi,g,h)/df(xi,g,h,t)
    xi=xf
    count+=1
    print('count={},\txf={}'.format(count,xi))
  print('==========================')
  print('root of f(x) = {}.'.format(xf))