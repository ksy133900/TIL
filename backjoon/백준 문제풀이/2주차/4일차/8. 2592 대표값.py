import sys
from collections import Counter
sys.stdin = open("8.txt", "r")

N = 10
numbers_list = []
for t in range(N):
    M = int(input())
    numbers_list.append(M)
    
count = Counter(numbers_list).most_common(1) 
# [(30, 3), (40, 2), (60, 2), (10, 1), (20, 1), (50, 1)]
# 횟수를 내림차순으로 정리하고 리스트 안 맨 앞에 있는 튜플을 출력 
# count = [(30,3)]

print(sum(numbers_list) // N) # 리스트 내 합계 / N = 37
print(count[0][0]) # 30

#count[0] = (30,3)
#30을 출력해야 하므로 [0][0]
