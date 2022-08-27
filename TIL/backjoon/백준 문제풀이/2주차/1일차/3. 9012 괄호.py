
T = int(input())
for _ in range(1,T+1) :
    w = input()
    
    # '()'가 한쌍 인 것이 VPS => 주어진 괄호를 ()로 묶어서 계속 공백으로 지워나갈 때
    
    # '()'가 계속 한쌍식 성립하여 다 지워진 후 공백만 남는다면 VPS라고 볼 수 있음.
    
    while '()' in w : # w에 '()' 있으면 반복
        w = w.replace('()','') # '()'를 ''로 바꾼다
    if w == '': # ''가 w안에 있으면
        print('YES') # YES
    else :
        print('NO') # 없으면 NO