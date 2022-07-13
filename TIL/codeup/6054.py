#2개의 정수가 공백을 두고 입력된다.
#두 불 값이 모두 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.
a,b=input().split()
print(bool(int(a)) and bool(int(b)))
