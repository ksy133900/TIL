#두 정수(a, b)를 입력받아 공백을 두고 입력된다.
#b의 값이 a의 값 보다 크거나 같으면 True , 같지 않으면 False 출력
a,b=input().split()
a=int(a)
b=int(b)
if b>=a:
    print('True')
else:
    print('False')