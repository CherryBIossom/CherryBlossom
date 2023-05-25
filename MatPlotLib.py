import numpy as n
import matplotlib.pyplot as mp
import matplotlib.cm as mc

# def sq(a):
  # return a*a

# x=n.arange(0.1,10,0.1)

# mp.xlim(0,10)
# mp.plot(x,sq(x),linewidth=3,label='$y$') # linewidth = 선 두께
# mp.legend(loc='upper left')
# mp.title('sex',loc='center')
# mp.show()
#mp.showfig('파일이름') = 파일에 저장

# mp.plot(x,0.5*x,label='y=0.5x')
# mp.plot(x,n.log(x),label='y=logx')

# mp.show()

# d=0.01
# x=n.arange(-5,5,d)
# y=n.arange(-5,5,d)
# X=n.meshgrid(x)
# Y=n.meshgrid(y)
# X,Y=n.meshgrid(x,y)
# # print(X)
# # print(Y)

# # 원 그리기
# Z=X*X+Y*Y
# levels=n.arange(1,45,3)
# fig,ax=mp.subplots()

# # 색깔 넣기
# im=ax.imshow(Z,interpolation='bilinear',cmap=mc.rainbow,extent=(-5,5,-5,5))

# CS=ax.contour(X,Y,Z,levels)
# ax.clabel(CS) # 숫자 표시 여부


# mp.plot(X,Y,marker='.',color='black',linestyle='none')
# mp.show()


list1=[]
with open('점수.txt') as file:
  for line in file:
    score=int(line.strip())
    list1.append(score)

x=n.array(list1)
hist=mp.hist(x,bins=10,rwidth=0.5,cumulative=True) # cumulative 는 누적할 경우 사용
mp.show()