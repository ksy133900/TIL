import sys

sys.stdin = open("_모음이보이지않는사람.txt")

TC = int(input())
for t in range(1,TC+1):
    word = input()
    word = word.replace('a','')
    word = word.replace('e','')
    word = word.replace('i','')
    word = word.replace('o','')
    word = word.replace('u','')
    print(f'#{t} {word}')