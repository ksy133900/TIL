import sys
sys.stdin = open("2953.txt", "r")

input = sys.stdin.readline

score_list = []
max_score = []
for _ in range(5):
    score_list.append(list(map(int,input().split())))
for i in score_list:
    max_score.append(sum(i))

max_sum = max(max_score)
max_index = max_score.index(max_sum)

print(max_index+1, max_sum)
    