import sys
sys.stdin = open("절댓값 힙.txt", "r")
import heapq
input = sys.stdin.readline

number_list = []

N = int(input()) # 18

for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(number_list,(abs(x),x)) 
        #abs(변수) = 절댓값 , number_list에 값을 넣을 때 절대값과
        #원래값을 쌍으로 같이 넣어줌으로 절대값을 기준으로 정렬을 한다.
    else :
        if not number_list:
            print(0)
        else:
            print(heapq.heappop(number_list)[1])