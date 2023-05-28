from matplotlib import pyplot as p
import numpy as n
import math as m
import seaborn as sea

J = 1
print('J =',J)
kT = float(input('Temperature(=/0) : ')) # 온도 입력
N = 20
print('N =',N)

def spin_field(N,M):
    return n.random.choice([-1,1], size=[N,M]) # '-1' 과 '1' 로 구성된 [NxM] 크기의 행렬 함수 정의

S=spin_field(N,N) # M = N, 초기 배열값을 갖는 행렬 생성


def Hamiltonian(S): # 해밀토니안 함수 정의
    Etmp = 0 # 처음 에너지 = 0

    for i in range(N):
        for j in range(N):
            if i==0: # 1열인 경우
                top=S[N-1][j] # 벽으로 막혀있는 윗 부분은 마지막 열로 대체
            else:
                top=S[1][j]
        
            if i==N-1: # 마지막 열인 경우
                bottom=S[0][j] # 벽으로 막혀있는 아랫 부분은 1열로 대체
            else:
                bottom=S[i+1][j]

            if j==0: # 1행인 경우
                left=S[i][N-1] # 벽으로 막혀있는 왼쪽 부분은 마지막 행으로 대체
            else:
                left=S[i][j-1]
        
            if j==N-1: # 마지막 행인 경우
                right=S[i][0] # 벽으로 막혀있는 오른쪽 부분은 1행으로 대체
            else:
                right=S[i][j+1]

            Etmp=Etmp-J*S[i][j]*(left+right+top+bottom)/2 # 에너지 계산
    
    return Etmp


def spin_field_sampling(): # 에너지 값의 차이에 따른 배열 샘플링 함수 정의
    if r>=1: # r 값이 1 이상일 경우
        Etmp=Hamiltonian(S_after) # 하나를 뒤집은 배열의 에너지 값을 얻는다.
        S=S_after # 기존 배열은 하나를 뒤집은 배열로 바뀐다.
        return S, Etmp
    elif r<1: # r 값이 1 미만일 경우
        p=n.random.uniform(0,1,1) # 0~1 사이의 실수 1개 생성
        if p<r: # 생성한 실수가 r 값보다 작을 경우
            Etmp=Hamiltonian(S_after) # 하나를 뒤집은 배열의 에너지 값을 얻는다.
            S=S_after # 기존 배열은 하나를 뒤집은 배열로 바뀐다.
            return S, Etmp
        else: # 생성한 실수가 r 값보다 클 경우
            Etmp=Hamiltonian(S_before) # 기존 배열의 에너지를 얻는다
            S=S_before # 기존 배열에서 바꾸지 않는다.
            return S, Etmp


for i in range(N*N*100):
    (x,y) = n.random.choice(N,2) # 0~N 사이의 정수를 랜덤으로 2개 생성해서 x,y 값에 대입
    S_before = S.copy() # 비교하기 위한 행렬 하나 복사
    S_after = S.copy() # 비교하기 위한 행렬 또 다른 하나 복사
    S_after[x][y] = (-1)*S_after[x][y] # S_after 배열에서 아무 원자 하나 뒤집기
    dU = Hamiltonian(S_after) - Hamiltonian(S_before) # 원자 하나를 뒤집은 배열의 에너지에서 기존 배열 에너지의 차
    r = m.exp(-dU/kT) # 에너지 값의 차이에 따른 r값 결정
    spin_field_sampling() # 샘플링 함수 반복
    S,Etmp=spin_field_sampling() # 배열과 에너지를 샘플링 함수에 의해 결정

print('Izing-model:') # 최종 배열 출력
print(spin_field_sampling()[0])
print('Energy:',spin_field_sampling()[1]) # 최종 배열에서의 에너지 값 출력

Sum=float(n.sum(S)) # 최종 배열의 전체 자기쌍극자 값의 합
if Sum != 0: # 다 더한 값이 0이 아닐 경우
    a = Sum/2 + float(N*N)/2 # a: 1의 개수 = 그 값의 절반 + 전체 개수의 절반
    b = float(N*N) - a # b: (-1)의 개수 = 전체 값에서 1의 개수를 뺀 값
elif Sum == 0: # 다 더한 값이 0일 경우
    a = b = float(N*N)/2 # 1과 (-1)의 개수가 같고 그 값은 전체 개수의 절반

print('1의 개수:',a)
print('(-1)의 개수:',b)

magnetization= float(a+b*(-1)) / float(N*N) # magnetization 함수 정의, magnetization = 1의 개수 + (-1)의 개수 / (N*N)
print('magnetization:',magnetization) 

 
sea.heatmap(S[:N, :N])
p.axis('off')
p.show()