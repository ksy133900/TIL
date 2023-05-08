import sys
input = sys.stdin.readline

N, G = input().split()
player = [input() for _ in range(int(N))]
player = list(set(player))	# set 중복 제거

if G == 'Y' :	# 윷놀이
    print(len(player))
elif G == 'F' :	# 같은 그림 찾기
    print(len(player) // 2)
elif G == 'O' :	# 원카드
    print(len(player) // 3)