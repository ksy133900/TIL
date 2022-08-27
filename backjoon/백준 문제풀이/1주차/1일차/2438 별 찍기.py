#첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
#https://www.acmicpc.net/problem/2438
T = int(input())
for a in range(1,T+1):
    print(a*"*".rjust(5))
    
        
