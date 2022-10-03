n = int(input())
w_list = []
for _ in range(n):
    w_list.append(input())
word_list = set(w_list)
w_list = list(word_list)
w_list.sort()
w_list.sort(key=len)
for i in w_list:
    print(i)
