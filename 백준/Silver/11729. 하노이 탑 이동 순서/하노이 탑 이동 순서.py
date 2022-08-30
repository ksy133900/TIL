def hanoi(n, a, b):
    if n > 1:
        hanoi(n-1, a, 6-a-b)              # 기둥이 1개 이상이면 그룹으로 묶인 n-1개 원판을 
                                          # 중간으로 먼저 다 옮긴다
    print(a, b)

    if n > 1:
        hanoi(n-1, 6-a-b, b)

n = int(input())

print(2**n -1)                               #총 이동해야 하는 횟수
hanoi(n, 1, 3) 