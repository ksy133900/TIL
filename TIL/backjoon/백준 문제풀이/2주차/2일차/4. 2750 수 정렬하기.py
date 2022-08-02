import sys
sys.stdin = open("수 정렬하기.txt", "r")

N = int(input()) # N개의 수 
numbers_list=[] # 빈 리스트 생성
for _ in range(1,N+1):
    
    number = int(input()) # range 범위만큼 숫자 입력 받고,
    
    numbers_list.append(number) # 입력 숫자 list에 저장
    
numbers_list.sort() # 오름차순으로 정렬

for n in numbers_list: # 리스트 순회해서 순회값들을 한줄씩 출력
    print(n)