#3의배수이면서 짝수 출력
n=int(input())
if n % 3==0 and n % 2==0:
    print('참')
else:
    print('거짓')