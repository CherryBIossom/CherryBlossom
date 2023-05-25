#print(10==100)
#x='3!'
#print(x!=6) # 팩토리얼을 쓰려면 따로 지정을 해 주어야 한다
#print(False)
#print(not True)
#print(False or True)
#print(True and False)
#print(True and True)
#A=input()
#B=float(A)
#if B>0:
  #print('양수')
#if B<0:
  #print('음수')
#if B==0:
  #print('0')

#print('아니 뭐가 문제지')
#a=int(input())
#if a%2==0 and a%3==0:
#  b='2, 3 공배수'
#elif a%2==0:
#  b='2 배수'
#elif a%3==0:
#  b='3 배수'
#elif a%2!=0 and a%3!=0:
#  b='2와 3 배수 둘 다 아님'
#print('{}는(은){}'.format(a,b))
#위에거 이거 왜 안 되지?

print('확인문제')
x=int(input('put a number: '))
if 10<x<20:
  print('조건에 맞습니다.')
else:
  print('조건에 안 맞습니다.')

#a=[1,2,True, abc,False]
#print(a)

#a=[1,2,[3,4,5]]

#print(a)
#print(a[2])
#print(a[2][0]) #2번째 문자열 안에서 0번째
#print(a[2][1:1]) #대괄호만 나옴

#b=[1,2,3]
#c=[4,5,6]
#print(b+c)

#for ㅎㅇ in range(18):  #단순 문장 반복 횟수로 가능
#  print('ㅂㅇㄹ')
#a=[1,2,3.14,[56]]       #리스트 세로로 나열 가능
#for ㅎㅇ in a:
#  print(ㅎㅇ)
#a=str('미안하다 이거 보여주려고 어그로 끌었다')        #문자열 세로로 나열 가능
#for a in a:
#  print(a)

print('확인문제')
numbers=[273,103,5,32,65,9,72,800,99]
for a in numbers:
  if a%2!=0:
    print('{}는 홀수입니다'.format(a))
  else:
    print('{}는 짝수입니다'.format(a))

print()
numbers=[273,103,5,32,65,9,72,800,99]
#for a in numbers:
#  if 0<a/10<1:
#    print('{}는{}자릿수입니다'.format(a,1))
#  elif 1<a/10<10:
#    print('{}는{}자릿수입니다'.format(a,2))
#  elif 10<a/10<100:
#    print('{}는{}자릿수입니다'.format(a,3))

for b in numbers:    
  print('{}는{}자릿수입니다'.format(b,len(str(b))))

print()
list_of_list=[
  [1,2,3],
  [4,5,6,7],
  [8,9]
]
#for a in list_of_list[0]:
#  print(a)
#for a in list_of_list[1]:
#  print(a)
#for a in list_of_list[2]:
#  print(a)

for a in list_of_list:
  for b in a:
    print(b)

print() 
numbers=[1,2,3,4,5,6,7,8,9]
output=[[],[],[]]

for number in numbers:
  output[number%3].append(number)
print(output)