import math

N = int(input())
number_list = []
if N == 0:
    number_list.append(1)
else:
    for i in range(1,N+1):
        number_list.append(i)
print(math.prod(number_list))
