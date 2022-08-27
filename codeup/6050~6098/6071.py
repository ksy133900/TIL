#임의의 정수가 줄을 바꿔 계속 입력된다.
#0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자


n=1 #처음 조건 검사를 통과(true) 위해 0 아닌 값을 임의로 저장
while True:
    a=input()
    a=int(a)
    if a == 0:
        break
    else:
        print(a)