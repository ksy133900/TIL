import sys
sys.stdin = open("10.txt", "r")

T = int(input())
for _ in range(T):
    word = input().split()
    result = [] # 뒤집은 단어 넣을 리스트
    for i in word:
        result.append(i[::-1])
        # 단어를 뒤집어서 리스트에 append()
        # result = ['I', 'ma', 'yppah', 'yadot']
    word_result = " ".join(result) # 공백을 기준으로 join.
    print(word_result)