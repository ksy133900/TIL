import sys
from pprint import pprint
sys.stdin = open("_파리퇴치.txt")

# M x M의 파리채가 N x N 의 행렬 내에서 왼쪽 상단부터 우측으로 한줄씩 겹치며 비교하면서 이동하면 될 것 같다고 생각했다.
# 다중 for문을 생각하는데 오래 걸린 것 같고 이 문제 코드 리뷰를 받고 싶습니다.

T = int(input())
for _ in range(1,T+1):
    N , M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    result = []

    for i in range(N-M+1):
        
        for j in range(N-M+1):
            sum = 0
            for k in range(M):
                for o in range(M):
                    sum += matrix[i+k][j+o]
                    result.append(sum)
        
                
    print(f'#{_}', max(result))
