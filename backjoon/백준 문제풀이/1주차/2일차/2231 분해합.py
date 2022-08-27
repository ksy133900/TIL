# 분해합 = 숫자 N과 + N의 각 자릿수의 합
# 198의 분해합은 198+1+9+8 = 216이다. 여기서 생성자는 198이다.
a = int(input())
answer = 0 # 생성자 값 넣어줄 공간

for i in range(1,a+1): # 1부터 입력값 a까지 순회 시작
    
    b = list(map(int,str(i))) # 순회값 i를 문자열로 변경하여 자릿수를 분해하고 다시 정수형으로 변환한 뒤 리스트에 저장 //
    
    result = i + sum(b) #순회값 i와 각 자릿수의 합 b를 더하여 result에 저장 // ex) 216 = 198 + 1+9+8 이라고 하면 (216 => result), (198 => i) , (1+9+8 = > sum(b))
    
    if a == result: #나의 입력값과 분해합이 같으면
        answer=answer+i # answer에 현재 생성자 값을 넣어준다.
        break #for문 종료
    if i == N :
        print(0)
print(answer) # 생성자 출력
        
    
    