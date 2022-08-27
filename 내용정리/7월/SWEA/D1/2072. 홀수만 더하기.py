a= int(input())
for i in range(0,a):
    numbers=map(int,input().split())
    sum=0
    for j in numbers:
        if j%2!=0:
            sum=sum+j
    print('#%d %d' % (i+1,sum))
            