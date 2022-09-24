import sys
input = sys.stdin.readline
result = 0
n = int(input())
x = sorted(list(map(int,input().split())))
y =list(map(int,input().split()))
y.sort(reverse=True)
for i in range(n):
    result += x[i] * y[i]
print(result)

