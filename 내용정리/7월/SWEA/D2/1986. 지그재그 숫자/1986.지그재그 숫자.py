i=int(input())
for a in range(0,i):
    x=int(input())
    result=0
    for c in range(1,x+1):
        if c%2==0:
            result-=c
        else:
            result+=c
    print('#%d %d' % (a+1,result))