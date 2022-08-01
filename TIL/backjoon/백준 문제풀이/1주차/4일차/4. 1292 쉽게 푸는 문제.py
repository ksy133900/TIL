# a=3 b=7
# 2+3+3+3+4 = 15

a,b = map(int,input().split())

numbers = [0]
#? 리스트는 0번부터 시작하는데, 우린 1부터 진행해야하므로 리스트에 미리 0을 넣어둔다. 
# [0,1,2, (2,3,3,3,4) ,4,4...]
# 넣지않으면 [1,2,2, (3,3,3,4,4) ,4,4...] 로 3+3+3+4+4 = 17이 될 것임.
sum = 0

for i in range(5): #문제에서는 range 1000
    for j in range(i): # range(i)는 0부터 i-1까지의 범위를 반환
        
        numbers.append(i)
        #위 2중 for문은 i를 j의 범위만큼 반복하는 것과 같음
# ex) i = 1 일 때 for j in range(1-1)  i는 1 범위 0이기 때문에 1을 append하면 number=[0,1]

#     i = 2 일 때 for j in range(2-1)  i는 2 범위 1이기 때문에 i를 한번 더 반복함 (2,2) append -> numbers = [0,1,2,2]

#     i = 3 일 때 for j in range(3-1)  1는 3 범위 2이기 때문에 i를 두번 더 반복함 (3,3,3) append -> number = [0,1,2,2,3,3,3]

#..... 계속 진행하면서 numbers에 append 된다.

for k in range(a,b+1): # a = 3 b = 7일 때 range(3,7)쓰면 3부터 6까지 범위지정이므로.. 범위의 끝 부분은 꼭 +1을 붙여주자. => range(a,b+1)
    sum += numbers[k] # sum에 numbers[3]값부터 numbers[7]까지 더한 값을 저장한다.
print(numbers)
print(sum)