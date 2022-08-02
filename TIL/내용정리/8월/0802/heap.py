import heapq
numbers = [0, 12345678, 1, 2, 0, 0,0, 0, 32]

heap = []

for number in numbers :
    
    if number != 0:
        heapq.heappush(heap, number)
    else: 
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))