t = list(map(int, input().split(':')))
hour = [h for h in range(1, 13)]
min_sec = [ms for ms in range(60)]

result = 0

for i in range(3) :
    for j in range(3) :
        for k in range(3) :
            if i != j and j != k and k != i :	
                if t[i] in hour and t[j] in min_sec and t[k] in min_sec :
                    result += 1

print(result)