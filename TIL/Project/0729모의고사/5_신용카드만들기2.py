import sys

sys.stdin = open("_신용카드만들기2.txt")


T = int(input())
for _ in range(1,T+1):

    card_numbers = input()
    list_card =[] 
    for i in card_numbers:
        list_card.append(i)
        # card_numbers[i] == '-' 썼다가 TypeError: string indices must be integers 오류발생 (문자열의 인덱스는 문자 안되고 정수이어야 함)
        # 그래서 빈 리스트를 생성하고 list_card =='-':로 바꿔주었다.                                
         
        if card_numbers[0] == '3' or card_numbers[0] == '4' or card_numbers[0] == '5' or card_numbers[0] == '6' or card_numbers[0] == '9' and list_card =='-':
            m = 1 #시작이 3 or 4 or 5 or 6 or 9이어야 하고, 리스트 내 '-'가 있으면 m을 1로 저장
        else :
            m = 0 #아니면 m을 0으로 저장
    
    print(f'#{_} {m}')    