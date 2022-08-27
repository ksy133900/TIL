import sys
sys.stdin = open("6.txt", "r")
N , M = map(int,input().split())
for i in range(N):
    print(input()[::-1])