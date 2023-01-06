n = int(input())
arr = [list(input()) for _ in range(n)]
answer = 0

for i in range(n):
    friend = 0
    for j in range(n): 
        if i == j: continue 
        if arr[i][j] == 'Y':
            friend += 1
        elif arr[i][j] == 'N': 
            for k in range(n): 
                if arr[j][k] == 'Y' and arr[i][k] == 'Y': 
                    friend += 1
                    break 
    answer = max(answer, friend)
print(answer)