import sys
sys.stdin = open("상금헌터.txt", "r")

T = int(input())
for _ in range(T):
        a , b = map(int,input().split())
        prize = 0
        if a == 1:
            prize += 5000000
        elif 1 < a <= 3:
            prize += 3000000
        elif 3 < a <= 6:
            prize += 2000000
        elif 6 < a <= 10:
            prize += 500000
        elif 10 < a <= 15:
            prize += 300000
        elif 15 < a <= 21:
            prize += 100000
        else :
            prize = 0
        if b == 1:
            prize += 5120000
        elif 1 < b <= 3:
            prize += 2560000
        elif 3 < b <= 7:
            prize += 1280000
        elif 7 < b <= 15:
            prize += 640000
        elif 15 < b <= 31:
            prize += 320000
        else:
            prize = 0
        print(prize)
        
        