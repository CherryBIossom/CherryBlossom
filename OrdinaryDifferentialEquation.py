import math
import matplotlib.pyplot as p

g=9.80665
l=1
pi=math.pi
dt=0.1

t=0
angle=30
x=l*math.sin(angle*pi/180)
w=0
friction=0.01
criterion=0.001

t_list=[]
x_list=[]
angle_list=[]
w_list=[]
t_list.append(t)
x_list.append(x)
angle_list.append(angle)
w_list.append(w)


def f(angle):
  return -friction*w-(g/l)*math.sin(angle*pi/180)

print('t\t x\t angle\t w')
print('{:6f}\t {:6f}\t {:6f}\t {:6f}'.format(t,x,angle,w))

while True:
  w=w+f(angle)*dt
  angle=angle+w*dt
  x=l*math.sin(angle*pi/180)
  t+=dt

  if (abs(angle)<criterion and abs(w)<criterion):
    break
  
  print('{:6f}\t {:6f}\t {:6f}\t {:6f}\t'.format(t,x,angle,w))

  t_list.append(t)
  x_list.append(x)
  angle_list.append(angle)
  w_list.append(w)



p.plot(t_list,angle_list,label='angle')
p.plot(t_list,w_list,label='w')
p.xlabel('time (s)', fontsize=12)
p.legend(loc='upper right')
p.show()