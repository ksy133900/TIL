import sys

sys.stdin = open("_민석이의과제체크하기.txt")
T = int(input())

for _ in range(1, T + 1) :
    h = [] #
    n, k = map(int, input().split()) # 총 학생 수 n과 과제 낸 사람 수 k
    data = list(map(int, input().split())) # 낸 사람의 번호!
    
# 안 낸 사람 번호를 출력하자
    for i in range(1,n+1): # 사람 수만큼 순회를 하고 (1,2,3,4,5)
        h.append(i) # h에 넣습니다
    result = list(set(h) - set(data)) # 두 리스트 사이에 중복이 안된 것을 출력하는 것으로
                                      # set 연산의 차집합이 떠올랐다.
    print(f'#{_}', *result)
    