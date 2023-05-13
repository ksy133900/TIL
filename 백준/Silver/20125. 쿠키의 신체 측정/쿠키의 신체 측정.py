from sys import stdin

arr = []
n = int(stdin.readline())
for i in range(n):
    arr.append(list(stdin.readline().rstrip()))

heo, l_leg, r_leg = 0, 0, 0


def find_heart():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '*':
                return (i, j), (i + 1, j)


head, heart = find_heart()


l_arm = arr[heart[0]][:heart[1]].count('*')
r_arm = arr[heart[0]][heart[1] + 1:].count('*')

for i in range(heart[0] + 1, n):
    if arr[i][heart[1]] != '*':
        last_heo = (i, heart[1])
        break
    else:
        heo += 1

for i in range(last_heo[0], n):
    if arr[i][heart[1] - 1] == '*':
        l_leg += 1

    if arr[i][heart[1] + 1] == '*':
        r_leg += 1


print(heart[0] + 1, heart[1] + 1)
print(l_arm, r_arm, heo, l_leg, r_leg)