import sys
sys.stdin = open("2. 태보태보 총난타.txt", "r")

taebo = input()
left = 0
left_punch = 0
right = 0
for i in taebo:
    if i == '@':
        left += 1
    if i == '(':
        left_punch = left
        left = 0
    
print(left_punch,end=' ')
print(left) 