import sys
sys.stdin = open("14888.txt", "r")

input = sys.stdin.readline

n = int(input())
a1,a2 = map(int,input().split())
m = list(map(int,input().split()))
print(m)