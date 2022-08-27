#아래 코드는 평균을 구하는 논리적으로 오류가 있는 코드입니다. 
#코드에서 오류를 찾아 원인을 적고, 수정하세요.

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
count += 1

print(total // count)

#count가 for문 안에 들어가 있지 않아서 for문이 다 끝나고
#단순하게 +1만 해서 print로 넘어가기 때문에 count=1이되고
#결국 print(55/1)이 결과값으로 나와 55가 출력되는 것임.
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(total // count)

# count += 1을 for문 안으로 집어넣어주자
# 출력값 5