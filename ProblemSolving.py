# pets=[
#   {'name': '구름', 'age':5},
#   {'name': '초코', 'age':3},
#   {'name': '아지', 'age':1},
#   {'name': '호랑이', 'age':1}
# ]

# print('#우리 동네 애완 동물들')
# for a in pets:
#   print('{} {}살'.format(a['name'], a['age']))
  
# numbers=[1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
# counter={}

# for number in numbers:
#   if number in counter:
#     counter[number] +=1
#   else:
#     counter[number] =1

# print(counter)


# key_lists=['A','B','C','D']
# value_lists=[4,3,2,1]
# # grades={'A'=4,'B'=3,'C'=2,'D'=1}
# grades=dict(A=4,B=3,C=2,D=1)

# print(grades)

# limit=10000
# sum_value=0
# a=0
# while limit>sum_value:
#   a=a+1
#   sum_value=sum_value+a

# print(a)


# max_value=0
# a=0
# b=0
# for i in range(101):
#   j=100-i
#   current=i*j
#   while current>max_value:
#     a=i
#     b=j
#     max_value=current
# print('최대가 되는 경우: {} * {} = {}'.format(a,b,max_value))


# aqua={}

# with open('test.txt','r') as test_file:
#   for a in test_file:
#     (name,habitat)=a.strip().split(',')
#     aqua[habitat]=name
# print(aqua)




b=2
c=3

def a():
  angle=b/c
  return angle

print(a())