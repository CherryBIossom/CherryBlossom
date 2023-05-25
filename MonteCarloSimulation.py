import numpy as n
import math as m

V=4
N_list=[100,1000,10000,100000]
Q_list=[]
error_list=[]

def H(x,y):
  if x*x+y*y<=1:
    return 1
  else:
    return 0

for N in N_list:
  Q=0
  i=0
  while i<N:
    x,y=n.random.uniform(-1,1,2)
    Q=Q+H(x,y)
    i+=1

  Q=4*Q/N
  error=(Q-n.pi)/n.pi # 구한 전체 넓이 - 실제 넓이 / 실제 넓이 = 에러율
  Q_list.append(Q)
  error_list.append(error)

print('Exact area = {}'.format(n.pi))
print()
for i in range(len(N_list)):
  print('N={}, approx. area = {}, error = {}'.format(N_list[i],Q_list[i],error_list[i]))


#실습

V=1.49365
N_list=[100,1000,10000,100000]
Q_list=[]
error_list=[]

def f(x,y):
  if (m.exp)**(-x**2)<=y:
    return 1
  else:
    return 0

for N in N_list:
  Q=0
  i=0
  while i<N:
    x,y=n.random.uniform(-1,1,2)
    Q=Q+f(x,y)
    i+=1

    Q=V*Q/N
    Q_list.append(Q)
    error=(Q-V)/V
    error_list.append(error)

print('real area = {}'.format(V))
print()
for i in range(len(N_list)):
  print('N={}, approx area={}, error={}'.format(N_list[i],Q_list[i],error_list[i]))