#시 분으로 이루어진 시각을 2개 입력 받아, 더한 값을 시 분으로 출력하는 프로그램을 작성하라.
import sys
sys.stdin = open("input.txt", "r")

T=int(input())
for a in range(0,T):
    si=0
    bun=0
    x,y,c,v=map(int,input().split())
    si=x+c
    if si > 12:
        si=si-12
    bun=y+v
    if bun > 60:
        bun=bun-60
        si=si+1
    print('#%d %d %d'% (a+1,si,bun))