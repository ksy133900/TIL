#1부터 n까지의 합
n=10
sum=0
m=0
while m<n:
  m+=1
  sum+=m
print(sum)   

n=10
sum=0
for i in range(n+1):
  sum+=i
print(sum)