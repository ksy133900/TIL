n = int(input())
m = map(int,input().split())
prime_number = 0 
for i in m:
    cnt = 0
    if i==1:
        continue
    for j in range(2,i+1):
        if (i % j == 0):
            cnt += 1
    if cnt == 1:
        prime_number += 1       
print(prime_number)