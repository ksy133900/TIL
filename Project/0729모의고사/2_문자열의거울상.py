import sys
sys.stdin = open("_문자열의거울상.txt")

# 문자를 뒤집고 b = d , d = b , p = q , q = p 이런식으로 접근하면 될 것 같다.

T = int(input())

for _ in range(1,T+1):
    word = list(input())
    word.reverse()

    for i in range(len(word)):
        if word[i]=='b':
            word[i]='d'
        elif word[i]=='d':
            word[i]='b'
        elif word[i]=='p':
            word[i]='q'
        elif word[i]=='q':
            word[i]='p'
    directory =''.join(word)        
    print(f'#{_} {directory}')
    
    