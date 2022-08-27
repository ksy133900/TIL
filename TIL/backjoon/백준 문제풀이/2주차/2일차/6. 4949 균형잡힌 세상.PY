from collections import Counter
import sys
sys.stdin = open("균형잡힌 세상.txt", "r")

for _ in range(7):

    words = input()
    
    while words in '()' or words in '[]':
        words = words.replace('()','')
        words = words.replace('[]','')

    print(words)

                    
                