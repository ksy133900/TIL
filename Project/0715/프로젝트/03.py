with open("data/fruits.txt", "r", encoding="utf-8") as f:
    line = f.readlines()
    dic = {}
    for i in line:
        i = i[:-1]
        dic[i] = dic.get(i, 0) + 1
        
with open("03.txt", "w", encoding="utf-8") as ff:
    for key in dic:
        ff.write(f"{key} {dic[key]}\n") 