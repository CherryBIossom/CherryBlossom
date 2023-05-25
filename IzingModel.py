from matplotlib import pyplot as p
import numpy as n
import math as m
import seaborn as se

def spin_field(N,M):
    return n.random.choice([-1,1], size=[N,M])

N=3
S=spin_field(N,N)

F=n.random.choice(N,2)
(x,y)=F[0],F[1]
S[x][y]=S[x][y]*(-1)
print(S[x][y])