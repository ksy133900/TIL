n,l = map(int,input().split())
fruit = sorted(list(map(int,input().split())))
for i in range(len(fruit)):
    if l >= fruit[i]:
        l += 1
print(l)