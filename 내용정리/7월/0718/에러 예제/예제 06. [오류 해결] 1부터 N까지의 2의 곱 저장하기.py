#아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다.
#코드에서 오류를 찾아 원인을 적고, 수정하세요.
N = 10
answer = ()
for number in range(N + 1):
    answer.append(number * 2)

print(answer)

#tuple(불변값)에는 속성 'append'가 불가능하다 append는 리스트에 적용

N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)

#answer을 빈 리스트 공간으로 바꿔주자