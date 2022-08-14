
import sys
sys.stdin = open("10773.제로.txt", "r")

T = int(input())
stack = []
for t in range(T):
    n = int(input())
    if n == 0:
        stack.pop()
        continue    
    stack.append(n)

print(sum(stack))
    
            
    