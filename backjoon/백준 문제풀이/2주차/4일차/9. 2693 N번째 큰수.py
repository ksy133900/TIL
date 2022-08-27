import sys
sys.stdin = open("9.txt", "r")

T = int(input())
for _ in range(T):
    A = list(map(int,input().split()))
    A.sort() # 오름차순 정렬
    print(A[7]) # 3번째로 큰수 A[7]