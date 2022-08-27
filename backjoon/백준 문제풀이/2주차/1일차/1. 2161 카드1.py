N = int(input())
numbers = [] 
garbage = [] # 버린 숫자들 들어갈 리스트

for t in range(1,N+1):
    numbers.append(t) # 1 2 3 4 5 6 7
while len(numbers) > 1:
    
    garbage.append(numbers.pop(0)) # numbers에서 맨 앞 값을 뺀 후 그 숫자를 garbage에 넣는다.
    numbers.append(numbers.pop(0)) # numbers에서 맨 앞 값을 뺀 후 그 숫자를 numbers의 맨 뒤에 넣는다.
    
for i in garbage:
    print(i, end = ' ') # 1,3,5,7,4,2
print(numbers[0]) # 마지막에 남는 카드의 숫자를 출력 (6)

#1 numbers = [2,3,4,5,6,7] , garbage = [1] ------- numbers = [3,4,5,6,7,2] ,garbage = [1]

#2 numbers = [4,5,6,7,2] , garbage = [1,3] ------- numbers = [5,6,7,2,4] ,garbage = [1,3]

#3 numbers = [6,7,2,4] , garbage = [1,3,5] ------- numbers = [7,2,4,6] ,garbage = [1,3,5]

#4 numbers = [2,4,6] , garbage = [1,3,5,7] ------- numbers = [4,6,2] ,garbage = [1,3,5,7]

#5 numbers = [6,2] , garbage = [1,3,5,7,4] ------- numbers = [2,6] ,garbage = [1,3,5,7,4]

#6 numbers = [6] , garbage = [1,3,5,7,4,2] ------- numbers = [6] , garbage = [1,3,5,7,4,2]

# len(numbers) = 1 로 while의 조건에 false이므로.. 반복 종료
