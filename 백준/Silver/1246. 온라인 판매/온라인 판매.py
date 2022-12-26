N, M = map(int, input().split())
li = sorted([int(input()) for _ in range(M)])
max_p = max_b = 0
for i in range(M):
    t = li[i] * ((M-i) if M-i <= N else N)
    if max_b < t:
        max_b = t
        max_p = li[i]
print(max_p, max_b)