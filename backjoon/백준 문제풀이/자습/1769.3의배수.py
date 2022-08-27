n = input()
cnt = 0
while len(n) > 1:
    number_list = []
    cnt += 1
    for i in n :
        number_list.append(int(i)) 
    n = str(sum(number_list))
    
print(cnt)
n = int(n)    
if n % 3 == 0:
    
    print('YES')
else:
    
    print('NO')       
