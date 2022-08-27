matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,0,1,2]
]

for i in range(3): # 행
    for j in range(4): #열
        print(matrix[i][j], end=" ")   # 행 우선 순회
    print()
    
for i in range(4): # 열
    for j in range(3): # 행
        print(matrix[j][i], end=" ")   # 열 우선 순회
    print()

    
n = len(matrix) # matrix 리스트 안에 있는 리스트의 갯수 [1,2,3,4] [5,6,7,8] [9,0,1,2] = 길이 3
m = len(matrix[0]) # matrix 리스트 안에 있는 0번째 리스트의 길이 [1,2,3,4] = 길이 4
print(n)
print(m)