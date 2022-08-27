import sys
sys.stdin = open('베스트셀러.txt','r')

t = int(input())
dic = {}
for _ in range(t):
    x = input()
    if x not in dic:
        dic[x] = 1
    else:
        dic[x] += 1
    
max_sold = max(dic.values())


best_seller=[]

for i in dic:
    if max_sold == dic[i]:
        best_seller.append(i)
        
best_seller.sort()
print(best_seller[0])