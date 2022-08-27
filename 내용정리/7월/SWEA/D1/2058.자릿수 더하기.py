a=int(input())
result=0
while a:
    result+=a%10
    a//=10
print(result)