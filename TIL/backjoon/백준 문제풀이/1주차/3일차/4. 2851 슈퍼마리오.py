
jumsu=0
numbers=[]
for i in range(10):
    numbers.append(int(input())) 
# 10개의 수를 입력받아 리스트에 넣는다.   
    
for j in numbers: # 예제2  [1, 2, 3, 5, 8, 13, 21, 34, 55, 89] #답 87
    
    jumsu += j # 리스트 순회하면서 jumsu에 계속 j값을 더해준다.
    
    if jumsu >= 100: # jumsu가 100이상이면
        # 55를 더하는 시점에서 jumsu = 142, j=55
        
       
         
        if jumsu - 100 > 100 - (jumsu-j) :  # 142와 87중 100에 더 가까운 것 찾기 (42와 13)
        # jumsu 142 - 100 >  100 - (142 - 55) 
        #          42     >  100 - (이전 더하기 값(87))
        #          42     >      13
        #                   
        # 13을 만들려면 100에서 87을 빼야함 142 - 55 = 87!
        #
        #                       
                         
                      
            jumsu = jumsu - j  
            # 점수에서 현재 j값을 빼준다 142-55 = 87
        break
            # 반복 탈출
print(jumsu)

