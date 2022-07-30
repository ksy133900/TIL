import sys
from collections import Counter
sys.stdin = open("_최빈수구하기.txt")

T = int(input())
for _ in range(1,T+1):
    # 숫자를 입력한 숫자 갯수만큼 입력 받고
    n = int(input()) 
    numbers = list(map(int, input().split()))
    # 입력받은 10개 숫자를 리스트에 저장
    most = Counter(numbers).most_common()[0][0]
    # Counter 함수와 most_common() 최빈값 함수를 이용하여 최빈값을 most에 저장
    print(f'#{n} {most}')