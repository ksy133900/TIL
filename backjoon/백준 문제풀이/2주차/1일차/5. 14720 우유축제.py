N = int(input())

numbers = list(map(int,input().split()))

cnt = 0
for i in range(N):
    if numbers[i] == cnt % 3:
        cnt += 1
print(cnt)