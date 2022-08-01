a=int(input())
for i in range(0,a):
    numbers=list(map(int,input().split()))
    print(('#%d %d' % (i+1, round(sum(numbers)/len(numbers)))))
    
    
    
    
