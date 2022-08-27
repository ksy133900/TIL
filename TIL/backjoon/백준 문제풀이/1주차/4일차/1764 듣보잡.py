import sys
sys.stdin = open('듣보잡.txt','r')
N,M = list(map(int,input().split()))
dict_ = dict()
# N의 크기만큼 듣도못한 사람 입력받기
for i in range(N):
    p = input()
    dict_[p] = "듣도못한"
    
list_ = []
for i in range(M):
    p = input()
    # 입력 받은 사람이 딕셔너리 키 중에 있는가
    if p in dict_:
        list_.append(p)
list_.sort()
print(len(list_))
for p in list_:
    print(p)


