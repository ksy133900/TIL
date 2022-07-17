with open("data/fruits.txt", 'r', encoding='utf-8') as f:
    a=f.readlines()
    print(a)
    cnt=0
    c=[]
    a=set(a)
    for i in a:
        k = i[:-1]
        if k.endswith('berry'):
            cnt+=1
            c.append(i)
print(cnt)   
with open("02.txt", 'w', encoding='utf-8') as fw:
    fw.write(f'{cnt}\n')
    for j in c:
        print(j)
        fw.write(j)