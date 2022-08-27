import sys
sys.stdin = open("2.txt", "r")

square = [[0]*100 for _ in range(100)]
  # 모든 x좌표와 y좌표는 1이상이고 100이하인 정수이다.
area = 0  
for _ in range(4): # 위 공간에 좌표를 찍어 4개의 직사각형 생성 = 4번 반복
    x1 , y1 , x2 , y2 = map(int,input().split()) # x는 가로 y는 세로

    
    for i in range(x1,x2): # 가로 길이 범위
        for j in range(y1,y2): # 세로 길이 범위
            square[i][j] = 1 # 순회하면서 해당 위치에 1을 넣는다.
            # x1, y1, x2, y2 = 1 2 4 4 
            
            # 첫 번째 사각형의 경우 i = 1 ~ 3 , j = 2 ~ 3 
            # square [1][2], [1][3], [2][2], [2][3], [3][2], [3][3]
            # (임의) square1 = [[0, 0, 1, 1, 0, 0, .....0*100]
            #                   [0, 0, 1, 1, 0, 0, .....0*100]
            #                   [0, 0, 1, 1, 0, 0, .....0*100]] = 면적(넓이) = 1+1+1+1+1+1 = 6
        
for a in square: # 위 for문으로 1이 추가된 square 순회
    area += sum(a) # area에 square에 있는 1을 다 더한 값을 저장한다.
print(area)
           
           