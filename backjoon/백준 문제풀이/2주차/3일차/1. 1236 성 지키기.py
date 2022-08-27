import sys
sys.stdin = open("성 지키기.txt", "r")


N , M = map(int,input().split()) # N이 행(가로) M이 열(세로)
protect = [list(input()) for _ in range(N)] #행렬 생성 (3,5)

cnt1,cnt2 = 0,0 # 행과 열에 각각 'x' 가 없으면 +1 할 변수


for i in range(N): # 행 단위로 순회하면서 "X"가 없는 행이 있으면 +1
    print(protect[i])
    if 'X' not in protect[i]:
         
        cnt1 += 1
        
print(cnt1)       
for i in range(M): # 열 단위 확인 시작.
    column_list = []
# 각 열의 요소 담을 리스트 생성
    for j in range(N):
        column_list.append(protect[j][i])
        # ex) i가 0일 때 j는 1,2,3 순회 => protect[0,0] , [1,0],[]
        
    if 'X' not in column_list: # 열 단위로 확인하여 'x'가 없으면 +1
        cnt2 += 1
# 행과 열 단위로 센 카운트 값들 중 큰 값을 출력하면 된다.   
    print(column_list)     
print(max(cnt1,cnt2))


