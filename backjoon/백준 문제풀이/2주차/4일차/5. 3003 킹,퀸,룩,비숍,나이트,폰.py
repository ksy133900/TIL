import sys
sys.stdin = open("5.txt", "r")
m = list(map(int,input().split()))

chess = [1,1,2,2,2,8]
for i in range(6): # 순회하면서 각 리스트의 [i]요소끼리 빼면 됨
    print(chess[i]-m[i],end=' ')