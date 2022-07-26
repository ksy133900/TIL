result=[] #빈 list 생성

for i in range(5): # for문을 5번 돌면서
    
    # 리스트에 정수형 값을 입력받아 sum 함수로 더한 후 result 리스트에 넣는다.
    result.append(sum(map(int,input().split()))) 

print(result.index(max(result)+1),max(result)) 
# result의 최댓값을 가지는 인덱스와 번호와 최댓값을 출력한다,
# 인덱스는 0부터 시작하므로 +1을 해서 출력해주도록 한다.

# 리스트명.index(max(값)) = > 최댓값의 인덱스명을 출력해줌