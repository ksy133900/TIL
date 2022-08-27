import sys
sys.stdin = open("_암호생성기.txt")

# 솔직히 문제가 이해 잘 안갔는데 그냥 조건들 잘 나와있어서
# 조건만 보고 푼 듯 하다.


# 첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 넣어준다. 리스트.pop(0) - 1
# 빼는 숫자는 1씩 늘어난다. 5까지 뺐으면 다시 빼는 숫자는 1이 되고 그 사이클을 반복한다.
# 숫자가 감소할 때 0 이하가 되면 암호문 맨 뒤에 0 넣고 반복을 종료함.
# 빼는 숫자가 하나씩 늘어나니까 변수로 i = 1 지정해주고 i += 1 이용해서 늘려나간다.


T = 10
for _ in range(1,T+1):
    C = int(input())
    password = list(map(int,input().split()))
    i = 1 # 뺄 숫자

    while True:
        if i > 5: # i
            i = 1
        number = password.pop(0) - i
        if number <= 0:
            password.append(0)
            break
        password.append(number)
        i += 1
    print(f'#{_}', *password)