import sys

sys.stdin = open("_퍼펙트셔플.txt")

TC = int(input())

for t in range(1, TC+1):
    N = int(input())
    words = list(input().split())
    result = []
    a = 0
    b = (N+1) // 2
    for i in range(N // 2):
        result.append(words[a]) 
        result.append(words[b])
        a += 1
        b += 1
    if N % 2 == 1:
        result.append(words[N//2])
    result = ' '.join(result)
    print(f'#{t} {result}')