import sys
sys.stdin = open("유학 금지.txt", "r")

word = input()
for i in word:
    if i == 'C':
        word = word.replace('C','')
    elif i == 'A':
        word = word.replace('A','')
    elif i == 'M':
        word = word.replace('M','')
    elif i == 'B':
        word = word.replace('B','')
    elif i == 'R':
        word = word.replace('R','')
    elif i == 'I':
        word = word.replace('I','')
    elif i == 'D':
        word = word.replace('D','')      
    elif i == 'G':
        word = word.replace('G','')     
    elif i == 'E':
        word = word.replace('E','')
print(word)   
    
    
    
    
    
    
    
    
    
#CAMBRIDGE