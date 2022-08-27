import sys
sys.stdin = open("대칭차집합.txt", "r")

A , B = (map(int,input().split()))
a = set(map(int,input().split()))
b = set(map(int,input().split()))

print(len(a ^ b)) #대칭 차집합 기호는 A ^ B
