t = int(input())
result = 0
while t >= 0:
    if t % 5 == 0:
        result = result + (t // 5)
        print(result)
        break
    t = t - 3
    result = result + 1
else:
    print(-1)
