#import sys
#sys.stdin = open("암기왕.txt", "r")

#T = int(input())

#for _ in range(T):

    
number = list(map(int,input().split())) # range 범위만큼 숫자 입력 받고,
number2 = list(map(int,input().split()))
cnt = 0
c = []
for n1 in number :
    for n2 in number2:
        if n1 == n2:
            c.append(1)
        else:
            c.append(0)
print(c)