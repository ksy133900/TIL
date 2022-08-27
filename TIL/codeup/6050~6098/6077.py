#정수 1개가 입력된다.
#(0 ~ 100)출력 1부터 그 수까지 짝수만 합해 출력한다.
x=int(input())
sum=0
for i in range(x+1):
    if i%2==0:
        sum=sum+i
print(sum)

    