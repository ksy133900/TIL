a=int(input())
for w in range(0,a):
    numbers = map(int,input().split())
    max = 0
    for i in numbers:
        if max < i:
            max = i
    print('#%d %d'%(w+1,max))
