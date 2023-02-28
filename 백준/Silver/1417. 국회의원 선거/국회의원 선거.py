import sys

N = int(sys.stdin.readline().rstrip())

vote = list() 
for i in range(0,N):
    vote.append(int(sys.stdin.readline().rstrip()))
    
answer = 0
m = max(vote)


while m!=vote[0] or vote.count(m)>=2:

    maxIndex = vote[1:].index(max(vote[1:]))+1

    vote[0]+=1

    vote[maxIndex]-=1

    answer += 1
    m = max(vote)

print(answer)