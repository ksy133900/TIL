#간단한 소인수 분해 N=2^a x 3^b x 5^c x 7^d x 11^e
# a,b,c,d,e 출력

#import sys
#sys.stdin = open("input.txt", "r")
T=int(input())
for u in range(0,T):
    a,b,c,d,e = 0,0,0,0,0
    x=int(input())
    while x % 2 == 0:
        a+=1
        x //= 2
    while x % 3 == 0:
        b+=1
        x //= 3
    while x % 5 == 0:
        c+=1
        x //= 5
    while x % 7 == 0:
        d+=1
        x //= 7
    while x % 11 == 0:
        e+=1
        x //= 11
    print("#%d %d %d %d %d %d" % (u+1,a,b,c,d,e))
        
        