N = int(input())

road = list(map(int, input().split()))

result = 0

for i in range(N): # road[i]부터 순회 시작
    
    for j in range(i+1, N): #road[i+1]부터 순회 시작
        
        if road[j] > road[j-1]: #  뒤의 길(원소)이 앞의 길(원소)보다 크면
            result = max(result, road[j] - road[i]) # 값을 빼고 result에 저장하고 가장 큰 값을 result에 갱신한다..
            
        else: # road[j] < road[j-1]면
            break # 두 번째 for문을 중단하고 첫번째 for문으로 가서 i를 하나 증가시키고(range) 
                  # 
print(result)

# 12 20 1 3 4 4 11 1