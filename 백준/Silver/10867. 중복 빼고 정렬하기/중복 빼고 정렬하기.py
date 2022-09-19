n = int(input())
n_list = sorted(set(list(map(int,input().split()))))
print(*n_list)