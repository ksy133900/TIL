import sys
sys.stdin = open("7. 킹.txt", "r")

direction = { # 8방향 이동값 딕셔너리
     'R' : (0,1),
     'L' : (0,-1),
     'B' : (1,0),
     'T' : (-1,0),
     'LT' : (-1,-1),
     'RT' : (-1,1),
     'RB' : (1,1),
     'LB' : (1,-1)
 }
k,s,n = input().split() # 킹,돌 위치와 이동할 횟수 A1 A2 5
 
# 8 x 8 체스판에서 A1 = (7,0),  k의 input값 'A1',   k[1] = 1,  8 - int(1) = 7
kx = 8 - int(k[1]) # king의 x좌표

# 아스키 코드표에서 A의 정수 표기는 65,  65 빼서 y좌표 0 만듦
ky = ord(k[0]) - 65 # king의 y좌표

# A1 = (kx,ky) = (7,0)

sx = 8 - int(s[1]) # 돌의 x좌표   8-2 = 6
sy = ord(s[0]) - 65 # 돌의 y좌표 65-65 = 0
# A2 = (sx,sy) = (6,0)

for i in range(int(n)): # (델타 탐색) 5번 이동.
    move = input() # 이동값 입력
    mx , my = direction[move] # mx와 my에 입력받은 이동값의 해당하는 딕셔너리 값을 저장.
                              # 처음 B일 때, mx = 1 my = 0 저장 
    if not (0 <= kx+mx < 8 and 0 <= ky+my < 8) : 
        #  이동 한 값이 위 조건을 만족하지 않으면 = (체스판의 범위를 벗어나면)
        continue # 해당 반복은 건너뜀.
    
    kx += mx # 범위를 벗어나지 않았을 때 킹의 위치 이동,
    ky += my
    
    if (kx,ky) == (sx,sy): # 킹과 돌의 위치가 겹쳤을 때,
        if not (0 <= kx+mx < 8 and 0 <= ky+my < 8 ): 
            # 체스판 범위 벗어난 경우
            
            kx -= mx  # 킹의 위치를 이동 전의 상태로 돌려놓는다.
            ky -= my  
            continue # 그리고 건너 뜀.
        
        sx += mx # 체스판 범위 내에 있을 때.
        sy += my # 킹이 움직인 만큼 돌에 이동값을 더해 움직여준다.
        
# (kx,ky) = (7,0)
# (sx,sy) = (6,0)
# 다시 알파벳과 숫자 합친 형태로 변환하여 출력.
print(chr(ky+65)+str(8-kx)) # y좌표 : 65 더해서 문자로 변환 chr(0+65) 
print(chr(sy+65)+str(8-sx)) # x좌표 : 8 - (현재x좌표) 빼서 문자로 변환
# 문자열 간의 덧셈은 두 문자를 합쳐줌.