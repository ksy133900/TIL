import sys

sys.stdin = open("_Flatten.txt")

n =  10

for t in range(1,n+1):
    dump = int(input())
    box = list(map(int,input().split()))
    
    while dump:
        mbox = max(box)
        nbox = min(box)  # 각 box 리스트 내 최댓값, 최솟값 저장
        mbox_index = box.index(max(box)) # 최댓값과 최솟값의 인덱스 값 저장
        nbox_index = box.index(min(box))
        
        box[mbox_index] -= 1 # box의 최댓값 인덱스의 값에서 -1
        box[nbox_index] += 1 #  box의 최솟값 인덱스의  값에서 +1
        
        # 최댓값 최솟값이 바뀌면 인덱스 값 이용해서 그 값들을 찾아 다시 평탄화 작업을 시작함.
        
        dump -= 1 # dump가 0될 때까지 반복
        
        
    print(f'#{t} {max(box)-min(box)}')