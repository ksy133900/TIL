import sys
sys.stdin = open("책더미.txt", "r")

a , b = map(int,input().split()) # 4,2
result = ''


for j in range(b): 
    # 책더미 갯수 순회 (더미 2개) 
    x = int(input()) 
    # 각 책더미의 높이 '2'
    
    y = list(map(int,input().split())) 
    #책 더미 높이만큼 리스트에 숫자 입력받기 (3,1)
    z = sorted(y, reverse=True)
    if y == z :
        result = 'YES'
        
    else :
        result = 'NO'
        
    if result == 'NO':
        break
print(result)
        
    
    
    # for w in range(x-1): # 책 더미 높이만큼 순회를 시작
    #     if y[w] > y[w+1]:
    #         print('YES')
    #         break
    #     else :
    #         print('NO')