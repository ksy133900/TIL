#정수 1개가 입력된다.
#1, 2, 3, 4, 5 ... 를 순서대로 계속 더해 합을 만들어가다가,
#입력된 정수와 같거나 커졌을 때, 마지막에 더한 정수를 출력한다.
x=int(input())
sum=0 # 더하는 수들의 합계
b=0  #더하는 수
while sum < x:
    b=b+1
    sum=sum+b
print(b)

n = int(input())

s = 0
t = 0
while s<n :
  t = t+1
  s = s+t
  
print(t)

