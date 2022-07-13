#두 정수가 공백을 두고 입력된다.
#입력된 두 정수(a, b) 중 큰 값을 출력하는 프로그램을 작성해보자.
a,b = input().split()
a=int(a)
b=int(b)
if a>b:
    print(a)
else:
    print(b)