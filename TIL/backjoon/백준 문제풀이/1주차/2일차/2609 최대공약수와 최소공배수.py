from math import gcd
from math import lcm

a,b = map(int,input().split())
#gcd << 최대공약수 구하는 함수
print(gcd(a,b))
#lcm << 최소공배수 구하는 함수
print(lcm(a,b))









#최대공약수
# list = []
# for i in range(min(a, b), 0, -1):
#     if a % i == 0 and b % i == 0:
#         list.append(i)
# print(list[0])

#a,b중 가장 작은 숫자부터 1까지 -1을 하며 for문을 실행
#a와 b가 %i로 딱 나누어떨어진다면 i는 a와b의 최대공약수이다

#최소공배수
# list = []
# for i in range(max(a, b), (a*b)+1):
#     if i % a == 0 and i % a == 0:
#         list.append(i)
# print(list[0])

    
