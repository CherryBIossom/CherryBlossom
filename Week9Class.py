# from urllib import request as r
# from bs4 import BeautifulSoup as B
# a=r.urlopen('http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108')
# # print(a.read())
# b=B(a,'html.parser')
# print(b)

# for c in b.select('lacation'):
#   print('도시:',c.select_one('city').string)
#   print('날씨:',c.select_one('wf').string)
#   print('최저기온:',c.select_one('tmn').string)
#   print('최고기온:',c.select_one('tmx').string)
#   print()

# url=('http://physicsedu.jnu.ac.kr/?r=physicsedu&c=196/207/841')
# html=r.urlopen(url)
# BsObj=B(html,'html.parser')


# for tbody in BsObj.select('tbody'):
#   for tr in BsObj.select('tr'):
#     check=str(tr.select_one('th').string)
#     if check=='전선' or check=='부필' or check=='교필':
#       nameList={코드=tr.find('td')}
#       for name in nameList:
#         print(name.get_text())

#       print('\n'.join([
#       '교과목 코드: {}',
#       '교과목 제목: {}',
#       '학점: {}',
#       '강의학점: {}',
#       '실습학점: {}',
#       '학기구분: {}'
#       ]).format(코드,제목,학점,강의학점,실습학점,학기구분))
#       print()







import numpy as n
# a=[[1,2],[3,4],[5,6]]
# a1=n.array(a)
# print(a1)
# print()

# b=n.zeros((2,3)) #0으로 된 2행 3렬 
# print(b)
# print()

# c=n.eye(4) # 4줄 항등행렬
# print(c)
# print()

# d=n.arange(3,10) #3이상 10미만 1차원 행렬
# print(d)
# print()

# e=n.arange(2.1,4.61,0.5) # 소수도 가능
# print(e)
# print()

# row,col=a1.shape
# print(row,col)

# for i in range(row):
#   for j in range(col):
#     print('{}행 {}열의 요소{}'.format(i,j,a[i][j]))


# f=a1.flatten()
# print(f)
# print(f[n.array([0,2,3])])
# print(a1>3) # a1행렬에서 3초과 불린
# print(a1[a1>3]) # a1행렬에서 3초과인 것들 출력


# g=n.array([1,2,3])
# h=n.array([4,5,6])
# print(g)
# print(h)
# print(n.add(g,h)) # 행렬 덧셈
# print(n.subtract(g,h)) # 행렬 뺄셈
# print(n.multiply(g,h)) # 행렬 곱셈
# print(n.divide(g,h)) # 행렬 나눗셈
# print(n.dot(g,h)) # 벡터 내적
# print(g*10) # 행렬 전체 상수곱
# print(g*[10,20,30]) # 요소별로 상수곱

# print(n.transpose([g,h])) # 행렬 교환
# i=n.transpose([g,h])
# print(n.dot([g,h],i)) # 2x3 행렬과 3x2 행렬 내적
# print(n.dot(i,[g,h])) # 행렬 내적의 순서가 바뀌면 값이 바뀜
# print()

# a2=[[1,2],[3,4]]
# j=n.linalg.inv(a2) # 역행렬
# print(j)

# print(n.dot(a2,j)) # 역행렬과 곱하면 항등행렬
# print(n.dot(j,a2)) # 순서가 바뀌어도 같음