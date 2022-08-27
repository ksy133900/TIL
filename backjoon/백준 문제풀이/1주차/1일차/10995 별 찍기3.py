#https://www.acmicpc.net/problem/10995
T=int(input())
if T == 1:
    print('*')
else:
    for a in range(T):
        if a%2 == 0 :
            b=print('* '*T)
        else:
            c=print(' *'*T)