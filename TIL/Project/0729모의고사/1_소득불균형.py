import sys
sys.stdin = open("_소득불균형.txt")

    
T = int(input())  # Test case 입력
for _ in range(1,T+1): # 전체 테스트 케이스 수  
    
    n = int(input()) # 사람 수
    numbers = list(map(int,input().split())) # 소득
    agv_number = sum(numbers)//n # 총 소득 / 사람 수
    humun = 0 # 평균 이하 소득 사람 수 카운트 할 변수 
    for i in numbers: # 리스트 순회
        if i <= agv_number: # 평균보다 소득이 낮으면
            humun += 1 # 1씩 더함
    print(f'#{_} {humun}') #출력
      
