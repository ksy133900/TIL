#numbers = [0, 20, 100]
#numbers.remove(max(numbers))
#print(max(numbers))


numbers = [0, 20, 100, 40]
max=numbers[0]
second=numbers[0]

for n in numbers:# 전체 반복을 한다.
    if max < n: # n이 최대보다 크다면
        second = max # 두큰수에 최대를 넣는다.
        max = n
    elif second< n < max:
        second = n
print(second)
