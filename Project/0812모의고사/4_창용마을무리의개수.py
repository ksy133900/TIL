import sys

sys.stdin = open("_창용마을무리의개수.txt")
from collections import deque

T = int(input())
for tc in range(1,T+1):
    N , M = map(int,input().split())
    maeul = [[] for _ in range(N+1)]
    for _ in range(M):
        v1,v2 = map(int,input().split())
        maeul[v1].append(v2)
        maeul[v2].append(v1)
    # print(maeul)
    visited = [False] * (N+1)
    q = deque()
    
    visited[0] = True
    cnt = 0
    
    for i in range(1, N+1):
        if visited[i] == False:
            cnt += 1
            q.append(i)
            visited[i] = True
            
        while q:
            cur = q.popleft()
            for adj in maeul[cur]:
                if visited[adj] == False:
                    q.append(adj)
                    visited[adj] = True
                    
    print(f'#{tc} {cnt}')       
    