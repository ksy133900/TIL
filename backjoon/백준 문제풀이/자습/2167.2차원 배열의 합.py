
import sys
sys.stdin = open("2167.txt", "r")

input = sys.stdin.readline


n , m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
K = int(input())
for t in range(K):
    result = 0
    i,j,x,y = map(int,input().split())
    for q in range(i-1,x):
        for w in range(j-1,y):
            result += matrix[q][w]
            
    print(result)
            