import sys
sys.stdin = open("유니크.txt", "r")
input = sys.stdin.readline

# 5
# 100 99 98
# 100 97 92
# 63 89 63
# 99 99 99
# 89 97 98

N = int(input()) # 인원 수
game = [[], [], []]
sum = []
# 1게임 당 N명이 각자 카드 1장씩 낸다.

for i in range(N):
    a, b, c = map(int, input().split()) # 플레이어의 카드
    game[0].append(a) # 각 게임마다 내는 숫자들로만 리스트 구성 (각 리스트 내에서 비교하기 위해서)
    game[1].append(b)
    game[2].append(c)


# game = [                              game[j]
#   [100,  100,   63,     99,    89]    game[0]
#   [ 99,   97,   89,     99,    97]    game[1]
#   [ 98,   92,   63,     99,    98]    game[2]
# ]  0점   92점   215점   198점   89점
# 

for i in range(N): # i = 인원 수 만큼 반복한다. (0~4) = 5번
    result = 0 # 각 플레이어가 3번의 게임에서 얻은 총 점수
    for j in range(3): # j = 행 갯수
        if game[j].count(game[j][i]) == 1:
            # game[j] 리스트에서 game[j][i] 요소를 하나씩 카운트 했을때 1이라면(유일하게 1개 있다면)
            result += game[j][i] #result에 해당 값을 더합니다.
            
    sum.append(result) #sum 리스트에 추가합니다
for i in sum:
    print(i)

    
# for i in range(N):
#     for j in range(3):
        