import sys

n=int(sys.stdin.readline())
card = [0] + [int(i) for i in sys.stdin.readline().split()]
dp = [0]+[99999999 for _ in range(n)]

for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i] = min(dp[i], dp[i-j]+card[j])
        
print(dp[-1])