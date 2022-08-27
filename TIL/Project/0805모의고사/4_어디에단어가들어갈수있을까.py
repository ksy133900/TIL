import sys
from pprint import pprint 
sys.stdin = open("_어디에단어가들어갈수있을까.txt")

# 퍼즐이라는 행렬을 생성하고. 행 단위로 순회를 시작하는데 puzzle[i][j]값이 1일 때마다 cnt += 1 을 해준다.
# puzzle[i][j]가 0 또는 마지막 열인 경우(둘다 성립해야함)에 cnt = k(문자 길이) 일 때 result에 +1을 해준다.
# 이후 현재의 값이 0일 경우 cnt를 다시 0으로 초기화한다.
# 행 순회 했으니 열 순회를 시작한다. 과정은 같고 range만 반대로 해주면 된다.

T = int(input())
for a in range(1,T+1):
    N , k = map(int,input().split())
    puzzle = [list(map(int,input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0 or j == N-1:
                if cnt == k:
                    result += 1
                if puzzle[i][j] == 0:
                    cnt = 0
                    
    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[j][i] == 1:
                cnt += 1
            if puzzle[j][i] == 0 or j == N-1:
                if cnt == k:
                    result += 1
                if puzzle[j][i] == 0:
                    cnt = 0
    print(f'#{a}', result)
            