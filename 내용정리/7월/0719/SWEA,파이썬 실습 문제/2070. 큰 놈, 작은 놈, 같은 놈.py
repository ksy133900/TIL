a=int(input())
for i in range(0,a):
    x,y=map(int,input().split())
    if x>y :
        print('#%d %s'% (i+1,'>'))
    elif x==y :
        print('#%d %s'% (i+1,'='))
    else:
        print('#%d %s'% (i+1,'<'))
    