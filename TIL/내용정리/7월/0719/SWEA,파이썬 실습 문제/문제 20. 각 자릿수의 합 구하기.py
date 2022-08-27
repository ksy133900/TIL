#str()없이
number=123
#100+23+3
a=number//100
b=((number%100)//10)
c=((number%100)%10)
sum=a+b+c
print(sum)

#다른 방법
number=123
result=0
while number:
    result+=number%10
    number//=10
print(result)
    #! result에 number의 나머지 값을 더하면서 number의 자릿수를 하나씩 줄이고, number가 0이되면 반복 종료
    #! result 값 1+2+3 = 6이 출력된다.


#str()
number=123
result=0
for i in str(number):
    result+=int(i)
print(result)
