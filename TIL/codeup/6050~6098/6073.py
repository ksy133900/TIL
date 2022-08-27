#정수 1개가 입력된다.
#1만큼씩 줄이면서 카운트다운 수가 0이 될 때까지 한 줄에 1개씩 출력한다.
a=int(input())
while True:
    a=a-1
    print(a)
    if a==0:
        break
