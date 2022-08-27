a=int(input())
for i in range(1,a+1):
    s = str(i)
    cnt = 0
    for j in s:
        if (j == '3') or (j == '6') or (j == '9'):
            cnt+=1
    if cnt==0:
        print(i,end=' ')
    else:
        print(cnt*'-',end=' ')