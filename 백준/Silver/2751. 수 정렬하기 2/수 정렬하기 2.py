import sys
input = sys.stdin.readline

n_list = []
n = int(input())
for _ in range(n):
    m=int(input())
    n_list.append(m)
n_list.sort()
for i in n_list:
    print(i)
       