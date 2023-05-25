#print('hello world')
#print(type(4)) #정수 (integer)
#print(type(4.0)) #실수 (floating number)
#print('5+7=',5+7) #덧셈
#print('5-7=',5-7) #뺄셈
#print('5x7=',5*7) #곱셈
#print("5/7=",5/7) #나눗셈
#print('5//2=',5//2) #나눗셈 몫
#print('5%2=',5%2) #나눗셈 나머지
#print('2^1=',2**1) #거듭제곱
#print(2+2-2*2/2*2) #기본적인 사칙연산 규칙을 따름
#print(2+2-2*2/(2*2)) #괄호 먼저 계산
#pi=3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
#print(pi) #소수점 15자리가 최대
#print(pi+2)
#print(pi/2)
#print(pi//2)
#print(pi%2)
#r=10.0
#print('radius=',r) #반지름
#print('area=',pi*r**2) #넓이
#print('circumference=',2*pi*r) #원주
number=100
#print(number) #100
number+=10 #number+10=
#print(number) #110
number-=20 #number-20=
#print(number)
number/=3 #//정수로 나오고 /실수로 나옴
#print(number)
number%=25 #나머지 5
#print(number) #5
number**=2 #5^2=
#print(number) #25
#a=number*2 #a=50
#print(a) #50
#print(number) #25, number는 바뀌지 않음
#print()
#print('확인문제')
#a=1
#a+=10
#a*=2
#print(a)
#b=5
#b**=2
#b%=5
#print(b)
#print()
#n1=input('a:') #n=number
#n2=input('b:')
#print(n1+n2) #숫자가 아닌 문자열, *중요!!!
#n1=int(input('a:'))
#n2=int(input('b:'))
#print(n1*n2) #input함수 앞에 int를 씌워주면 문자가 아닌 숫자가 된다.
#n3=float(input('c:'))
#print(n3) #int는 정수만 취급 float을 써야 실수취급
#print(type(3.14))
#print(type(int(3.14)))
#print(2+5)
#print(str(2)+str(5))
#print()
#print('확인문제')
#a=input('str: ')
#b=input('str: ')
#print(a,b)
#print(b,a)
#print()
#a=str('좋은아침입니다')
#b=str('안녕하세요')
#print()
#c=a
#a=b
#b=c
#print()
#a,b=b,a
#print(a,b)
#a='미안하다 이거 보여주려고 어그로 끌었다 {} 실화냐?'.format('내 파이썬 실력')
#print(a)
#print()
#b='{:+07d}'.format(314) # 7자리중 맨 앞 +붙이고 0으로 이은다음 끝에 314 
# d는 정수 f는 실수 g는 실수에서 0삭제
#print(b)
#c='{:+011f}'.format(3.14) # +다음 숫자가 출력 되고 나머지 0
#print(c)
#d='{:+07g}'.format(3.14) # 0이 나옴
#print(d)
#f='{:5g}'.format(3.14) # 0이 안 나옴
#print(f)
#z='{:.11f}'.format(3.14159265358979323846) # '.'<<소수점 11자리 제한, 그 뒤는 반올림
#print(z)
#print()
#g='Cherry_Blossom'
#print(g.upper()) #전부 대문자
#print(g.lower()) #전부 소문자
#print('Cherry_Blossom'.upper()) #바로 쓰는 것도 가능
#h=g.lower() #다른 인자로 바꾸어서 사용 가능
#print(h)
#print(h.capitalize()) #첫 글자만 대문자
#print()
#i="   Cherry_Blossom   "
#print(i)
#print(i.strip()) # 공백이 사라짐
#print(i.lstrip()) # 왼쪽 공백이 사라짐
#print(i.rstrip()) # 오른쪽 공백이 사라짐
#j=i.lstrip()
#k=i.rstrip()
#print(j,'length=', len(j)) # 왼쪽 공백이 줄어서 17자리
#print(k,'length=', len(k)) # 오른쪽 공백이 줄ㅇ어서 17자리
#print()
#l='Cherry_Blossom'
#print('h' in l) # h가 있다
#print('c' in l) # c가 없다(소문자)
#print()
#짝수='2, 4, 6, 8, 10'
#print(짝수)
#print(짝수.split(','))
#print(짝수.split(', ')) #뛰어쓰기도 포함시킨다
#홀수='1,3,5,7,9'
#print(홀수.split(','))
#print()
#print('확인문제')
#a=input('첫 번째 숫자: ')
#b=input('두 번째 숫자: ')
#print()
#print('{} + {} = {}'.format(a,b,int(a)+int(b)))

a='{:d}'.format(123)
b='{:5d}'.format(123)
c='{:+5d}'.format(123)
d='{:05d}'.format(123)
e='{:+05d}'.format(123)
f='{:f}'.format(1.23)
g='{:5f}'.format(1.23)
h='{:+5f}'.format(1.23)
i='{:05f}'.format(1.23)
j='{:+05f}'.format(1.23)
#f는 무적권 앞에서부터 시작하며 +-기호만 의미 있다. 0의 개수 조절 불가능
k='{:g}'.format(1.23)
l='{:7g}'.format(1.23)
m='{:07g}'.format(1.23)
n='{:+7g}'.format(1.23)
o='{:+07g}'.format(1.23)
#p='{:.f}'.format(1.23456789)
q='{:.7f}'.format(1.23456789123456789)
#r='{:.+7f}'.format(1.23456789)
s='{:.07f}'.format(1.23456789123456789)
#t='{:.+07f}'.format(1.23456789)
#소수점자리 제한하는'.'는(은) +-기호가 들어가면 에러뜸 0의미없음, 반올림함
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)
print(m)
print(n)
print(o)
#print(p)
print(q)
#print(r)
print(s)
#print(t)