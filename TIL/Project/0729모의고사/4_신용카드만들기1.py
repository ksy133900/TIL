import sys

sys.stdin = open("_신용카드만들기1.txt")


T = int(input())
for _ in range(1,T+1): #테스트케이스
    m = 0
    k = 0
    N = 0
    card_numbers = list(map(int,input().split())) # 카드 목록을 리스트로 받음
    for i in card_numbers[0::2]: # card_number 리스트를 0번부터 2칸씩 가면서 슬라이싱 한 값들을 순회한다. 홀수자리 체크
        m += i*2 # 순회할때마다 i에 있는 값을 m에 더해준다. 홀수자리 숫자들 x2하고 더해준다.
  
    for j in card_numbers[1::2]: #위와 같으나 리스트의 1번부터 2칸씩 가면서 슬라이싱 한 값들을 순회. 짝수자리 체크
        k += j # 순회할때마다 j에 있는 값을 k에 더해준다.
        
    while ((k+m)+ N) % 10 != 0: # (k+m)+N) % 10 의 나머지가 0이 아니면!
        N = N+1 # N에 1을 더한다. (나머지가 0이 될 때까지 N에 1을 계속 더한다.)
                  
    print(f'#{_} {N}')    



        