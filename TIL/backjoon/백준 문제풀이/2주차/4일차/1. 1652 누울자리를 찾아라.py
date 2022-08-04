import sys
sys.stdin = open("1.txt", "r")

N = int(input()) #방의 크기
word = [list(input()) for _ in range(N)] # 5x5 행렬 생성

result = 0 # 가로(행)로 누울 자리 갯수 저장할 공간
result2 = 0 # 세로(열)로 누울 자리 갯수 저장할 공간

for i in range(N): 
    cnt = 0  # 각 행이나 열 내에서 비교하는 것이기 때문에 하나의 순회가 끝나면
    cnt2 = 0 # cnt,cnt2를 0으로 초기화 하고 다시 순회 시작.
    
    for j in range(N): # 행을 기준으로 '.' 확인
        if word[i][j] == '.':
            cnt += 1  
        else:           # '.' 있으면 +1 없으면 0
            cnt = 0
        if cnt == 2:   # '.'을 2번 만나서 cnt가 2가 됬을경우
            result += 1 # result에 1을 더함.
                     
        if word[j][i] == '.': # 열 기준으로 '.' 확인
            cnt2 += 1
        else:                 # '.' 있으면 +1 없으면 0
            cnt2 = 0
        if cnt2 == 2:       # '.'을 2번 만나서 cnt가 2가 됬을경우
            result2 += 1    # result에 1을 더함.

# 정사각형 행렬, 가로 세로의 range는 같다.
# range(N)에서 N이 5이므로 10~28줄의 과정을 5번 반복함

print(result,result2) #행과 열에서 누울 수 있는 공간의 결과 출력.