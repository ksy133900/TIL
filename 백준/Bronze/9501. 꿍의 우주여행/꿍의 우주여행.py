import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n, d = map(int, input().split())
    result = 0
    for j in range(n):
        v, f, c = map(int, input().split())
        if f / c * v >= d: result += 1
    print(result)