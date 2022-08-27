import sys
sys.stdin = open("7. 세로 읽기.txt", "r")
input = sys.stdin.readline

s = [[0] * 15 for i in range(5)]
       
for i in range(5):
    word = list(input())
    
    for j in range(len(word)):
        s[i][j] = word[j]
for i in range(15):
    for j in range(5):
        if s[j][i] == 0:
            continue 
        else:
            print(s[j][i], end='')
        