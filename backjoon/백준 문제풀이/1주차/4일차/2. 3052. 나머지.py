import sys
sys.stdin = open('나머지.txt','r')

numbers = []
for _ in range(10):
    n = int(input())
    numbers.append(n % 42)

print(numbers)
result = set(numbers)
print((len(result)))