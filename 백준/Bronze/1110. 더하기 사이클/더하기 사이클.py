n = int(input())
number = n
result = 0
while True:
    x = number // 10
    y = number % 10
    z = (x + y) % 10
    number = (y * 10) + z
    
    result += 1
    if number == n:
        break
print(result)