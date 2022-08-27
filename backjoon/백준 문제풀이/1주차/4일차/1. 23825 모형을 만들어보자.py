# 2개 정수 입력
S,A=map(int,input().split()) 

# SASA만들려면 둘다 2개씩 있어야 함 홀수는 생각할 필요 없고
# 두 정수 중 최솟값을 뽑아 //2 를 한 값을 출력
result = min(S,A)
answer = result//2
print(answer)