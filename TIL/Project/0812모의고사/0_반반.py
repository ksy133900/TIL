import sys

sys.stdin = open("_반반.txt")
from collections import Counter

TC = int(input())
for _ in range(1,TC+1):
    s = []
    word = input()
    count = Counter(word)
    value = count.values()
    
    for i in value:
        if i % 2 == 0:
            s.append('True')
            

    if len(count.keys()) == 2 and s.count('True') == 2:
        print(f'#{_} Yes')
    else:
        print(f'#{_} No')
   
 