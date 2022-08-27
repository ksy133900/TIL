a=int(input())
for i in range(0,a):
    x,y=map(int,input().split())
    print('#%d %d %d' % (i+1,x//y,x%y))
