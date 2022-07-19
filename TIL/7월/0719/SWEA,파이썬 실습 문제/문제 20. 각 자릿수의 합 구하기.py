#str()없이
number=123
#100+23+3
a=number//100
b=((number%100)//10)
c=((number%100)%10)
sum=a+b+c
print(sum)

#str()
number=123
result=0
for i in str(number):
    result+=int(i)
print(result)
