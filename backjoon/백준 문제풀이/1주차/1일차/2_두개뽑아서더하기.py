# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    for i in range(len(numbers)): # numbers의 [0]부터 리스트(길이)만큼 순회 
        
        for j in range(i+1,len(numbers)): #numbers[i]의 다음 값 부터 순회 
            
            if numbers[i] + numbers[j] not in answer: # numbers[i]+number[j]값이 answer에 없다면
                
                answer.append(numbers[i] + numbers[j]) # 해당 값 answer에 할당
                
                answer.sort() #오름차순으로 정렬
    return answer
print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
