n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))
 
bridge = [0] * w    
weight, time = 0, 0    
 
while True:
    out = bridge.pop(0)   
    weight -= out 
 
    if trucks:  
        if weight + trucks[0] <= l:   
            bridge.append(trucks[0])   
            weight += trucks[0] 
            trucks.pop(0)  
        else:   
            bridge.append(0)   
    time += 1   
 
    if not bridge:    
        break    
print(time)