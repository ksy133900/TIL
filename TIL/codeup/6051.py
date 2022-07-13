#두 정수(a, b)를 공백으로
#a의 값이 b의 값과 서로 다르면 True
#같으면 False 를 출력하는 프로그램을 작성해보자.
a,b=input().split()
a=int(a)
b=int(b)
if a!=b:
    print('True')
else:
    print('False')
