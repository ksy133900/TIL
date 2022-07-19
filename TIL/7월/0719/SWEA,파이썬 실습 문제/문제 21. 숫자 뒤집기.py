number = 1234
# 4321 = 4000+300+20+1
a = number//1000 # 1
b = (number%1000) # 나머지 234
c = ((b//100)*10) # 234//100*10 = 20
d = (((number%100)//10)*100) #1234를 100으로 나눈 나머지 34를 다시 10으로 나누고 나온 몫3에 x100 = 300
e = ((number%10)*1000) #1234를 10으로 나눈 나머지 4에 x1000 = 4000
f = (e+d+c+a) # 4000+300+20+1 = 4321
print(f) # 답 : 4321

#다른 방법
number = 1234
result=0
while number:
    result=result*10 #! 이전 result 결과에 10을 곱한다
    result=result+number%10 #! result에 number%10값을 더해준다
    number//=10 #! number의 자릿수를 깎는다
print(result)

#! 1) result = 0     + 1234%10 = 4->  0+4= 4     , number = 1234//10 = 123
#! 2) result = 4*10  + 123%10 = 3 ->  40+3= 43   , number = 123//10 = 12
#! 3) result = 43*10 + 12 %10 = 2 -> 430+2=432   , number = 12//10 = 1
#! 4) result = 432*10+ 1%10 = 1   -> 4320+1=4321 , number = 1//10 = 0
#! 5) number = 0 이므로 반복이 종료되며 result 값 4321이 출력된다.
