import sys
sys.stdin = open("TGN.txt", "r")

N = int(input())
for _ in range(N):
    r,e,c = map(int,input().split())

    if r == (e-c): # 광고 전 수익 == (광고 후 수익 - 광고 비용)
        print('does not matter') # 수익도 없는데 굳이 광고를? .
        
    elif r > (e-c):# 광고 전 수익 > (광고 후 수익 - 광고비용)
        print('do not advertise') # 적자났음 광고 하면 안됨
        
    else: # 광고 전 수익 < (광고 후 수익 - 광고 비용)
        print('advertise') # 광고하자
    
        