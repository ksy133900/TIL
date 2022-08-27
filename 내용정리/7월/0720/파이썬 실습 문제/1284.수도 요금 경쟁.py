#import sys
#sys.stdin = open("1284.txt", "r")
T = int(input())
for a in range(0,T):
    P, Q, R, S, W = map(int,input().split()) #!  설명한 대로 P, Q, R, S, W(1 ≤ P, Q, R, S, W ≤ 10000, 자연수)가 순서대로 공백 하나로 구분되어 주어진다
    cost_A = W*P  #! A사 비용 - 1리터당 P원 (한달간 사용하는 수도 양)*(1리터당 돈) =W*P
    cost_B = Q #! B사 비용- 월간 사용량이 R리터 이하인 경우 요금은 기본 요금만 청구 -> COST_B=Q
    if R < W :         #! R 리터보다 많은 양을 사용한 경우
        cost_B += (W-R)*S #! 초과량에 대해 1리터당 S원의 요금을 더 내야 한다.
                       #! (나의 사용량 W에서 월간 사용량 R을 뺀 값에서 초과량을 곱한만큼을 더해준다.)
                        #! (W-R)*S
    c = min(cost_A,cost_B) #! min함수로 두 기업 간 더 작은 비용을 찾아 c에 넣고
    print('#%d %d'% (a+1,c)) #! #케이스 c를 출력합니다.