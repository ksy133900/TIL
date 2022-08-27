import sys
sys.stdin = open("6. 카드 놀이.txt", "r")

a = list(map(int,input().split()))
b = list(map(int,input().split()))
a_cnt = 0
b_cnt = 0
win = [0]
for i in range(10):
    if a[i] > b[i]:
        a_cnt += 3
        win.append('A')
    elif a[i] == b[i]:
        a_cnt += 1
        b_cnt += 1
    else:
        b_cnt += 3
        win.append('B')
print(a_cnt,end=' ')
print(b_cnt)
if a_cnt > b_cnt:
    print('A')
elif a_cnt == b_cnt:
    if win[-1] == 'A':
        print('A')
    elif win[-1] == 'B':
        print('B')
    else:
        print('D')
else:
    print('B')