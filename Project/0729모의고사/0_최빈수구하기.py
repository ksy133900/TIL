import sys
from collections import Counter
sys.stdin = open("_최빈수구하기.txt")

T = int(input())
for _ in range(1,T+1):
    # 입력한 숫자만큼 반복 (for문을 반복)
    n = int(input()) 
    #(테스트 케이스 1~10까지 입력 예정)
    numbers = list(map(int, input().split()))
    # 입력받은 숫자를 리스트에 저장
    most = Counter(numbers).most_common()[0][0]
    # Counter 함수와 most_common() 최빈값 함수를 이용하여 최빈값을 most에 저장
    print(f'#{n} {most}')