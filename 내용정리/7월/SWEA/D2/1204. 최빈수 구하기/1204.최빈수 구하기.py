from collections import Counter
import sys
sys.stdin = open("input.txt", "r")
T=int(input())
for a in range(1,T+1) :
    numbers=list(map(int,input().split()))
    c = Counter(numbers)
    mode = c.most_common(1)
    print(f'#{a} {mode[0][0]}')