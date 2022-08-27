import sys
sys.stdin = open("7.txt", "r")
m = int(input())
cup = [1,2,3]
for _ in range(m):
    a , b = map(int, input().split())
    x , y = cup.index(a), cup.index(b)
    cup[x], cup[y] = cup[y], cup[x]
print(cup[0])
