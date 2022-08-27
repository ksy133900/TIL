import sys
sys.stdin = open("2675.txt", "r")

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    r , s = input().split()
    word_list = []
    for i in range(len(s)):
        for j in range(int(r)):
            word_list.append(s[i])
    print(''.join(word_list))