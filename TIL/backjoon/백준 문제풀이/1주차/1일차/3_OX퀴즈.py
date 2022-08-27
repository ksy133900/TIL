# https://www.acmicpc.net/problem/8958
# 8958
import sys
sys.stdin = open("3_OX퀴즈.txt")

T = int(input())
for a in range(T): # 테스트 케이스 갯수
    
    x = input() # 문자열 입력값 할당
    sum = 0 # 점수값 = 0
    Correct = 1 # 'O'을 만났을 때 sum을 1씩 증가시켜야 하므로 Correct 값은 1로 시작
    
    for i in x: # 문자열 순회
        if i == 'O': # i == 'O'면 
            
            sum += Correct #  sum에 Correct값을 더해준다.
            Correct += 1
            # 'O'를 만났으므로 correct 값을 1 증가시킨다.
        else:
            Correct = 1 # 'O'가 아닌경우('X'만난 경우) Correct값을 1로 변경한다.
    print(sum)    