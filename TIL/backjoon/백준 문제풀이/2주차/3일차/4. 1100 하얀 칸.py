# TIP) 흰색 칸들의 인덱스 값 합은 짝수이고 검은 칸들은 홀수이다.

# matrix = []
# for _ in range(8):
#     a = list(input())
#     matrix.append(a)
# print(matrix)

import sys
sys.stdin = open("하얀칸.txt", "r")
matrix = [list(input()) for _ in range(8)] 
cnt = 0
# 8x8 행렬 N x M -> N은 INPUT M은 열
for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            if matrix[i][j] == 'F':
                cnt += 1
print(cnt)
