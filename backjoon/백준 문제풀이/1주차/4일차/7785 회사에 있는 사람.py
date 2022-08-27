t = int(input())
dic={}
for _ in range(t):
    h, s = input().split()
    
    if s == 'enter':
        dic[h] = 'enter'
    else :
        if dic[h]:
            del dic[h]
for humun in sorted(dic, reverse=True):
    print(humun)