import sys
sys.stdin = open("3. 오타맨 고창영.txt", "r")

T = int(input())
for _ in range(T):
    i,word = input().split()
    #print(word)
    i = int(i)
    word = list(word)
    word.pop(i-1)
    #for i in word[1]:
        
    print("".join(word))
    

    