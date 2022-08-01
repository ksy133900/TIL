import sys
sys.stdin = open('숫자 카드.txt','r')

T = int(input())
card = list(map(int,input().split()))
U = int(input())
card2 = list(map(int,input().split()))

dic = {}

for i in card:
    dic[i] = dic.get(i,0) + 1
    
for i in card2:

    if i in dic: print(dic[i], end=" ")
    else: print(0, end=" ")
    
