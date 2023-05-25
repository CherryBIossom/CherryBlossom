#딕셔너리
#a={'name':'이거보여주려고어그로끌었다'}
#print(a)
  
#b={'이름':'최우준', '성별':'남성','키':'2m','얼굴':'잘생김','몸무게':['46','50','56']}
#print(b)

#요소 추가
#['키']='value'
#b['핸드폰']='s10 5g'
#print(b)

#요소 수정 이름['키']='다른 값'
#b['키']='181cm'
#print(b)

#요소 제거 del 이름['키']
#del b['성별']
#print(b)

#요소 접근 이름['키'[0~]]]
#print(b['몸무게'][2])

#딕셔너리에서 요소 추출
#d=input()
#c=b.get(d) #괄호 안에 키 값
#print(c)

print('연습문제')
print()
# pets=[
#   {'name': '구름', 'age':5},
#   {'name': '초코', 'age':3},
#   {'name': '아지', 'age':1},
#   {'name': '호랑이', 'age':1}]
# print('#우리 동네 애완 동물들')
# for a in pets:
#   print('{} {}살'.format(a['name'],a['age']))

numbers=[1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3,]
counter={}

# for c in a:
#  b=cfor c in a:
#  b[c]=a.count(c)

for number in numbers:
  if number in counter:
    counter[number] +=1
  else:
    counter[number]=1
  
print(counter)

#print()
#print(type(range(5)))
#print(range(5))
#print(list(range(5)))

# a=[]
# for b in range(0,10,1):
#   a.append(b+b)
# print(a)
# # 위와 아래가 같다
# a=[b+b for b in range(0,10,1)]
# print(a)

#a=''.join(['a','b','c'])
#print(a)

# #연습문제
# key_lists=['A','B','C','D']
# value_lists=[4,3,2,1]
# grades={}

# #방법 1
# grades['A']=4
# grades['B']=3
# grades['C']=2
# grades['D']=1

# print(grades)

# #방법 2
# for a in range(len(key_lists)):
#  grades[key_lists[a]]=value_lists[a]
  
# print(grades)

# #방법 3
# grades= {key_lists[a]: value_lists[a] for a in range(len(key_lists))}

# print(grades)

# limit=10000
# sum_value=0
# a=list(range(1,142))
# while 100<b:
#   b=sum(a)
#   print(len(b))

# limit=10000
# sum_value=0
# a=list(range(sum_value,limit))
# print(a)