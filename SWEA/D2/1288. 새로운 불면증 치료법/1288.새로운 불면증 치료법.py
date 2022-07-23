# 1. 각 테스트 케이스마다 n을 문자열 형태로 입력받아 정수형으로 변환한 값을 value에 할당하고,
# 2. 각 자리수의 번호를 센 횟수가 담겨질 data 리스트를 정의한다.
# 3. 이후 반복문을 통해 n의 각 자리수를 하나씩 확인하여 
# 4. 그 값을 인덱스로 하여 data 리스트의 요소를 1 증가시킨다.
# 5. 만약 리스트의 요소들 중 0이 없을 경우 0부터 9까지의 모든 숫자가 최소 한번씩은 세어진 것
# 6. 해당 테스트 케이스 번호와 함께 정수형 n 을 출력하고 반복문을 종료한다.
# 7. 0이 아직까지 존재하는 경우 value값과 현재의 n 값을 더하여 문자열로 변환해 값을 갱신한다.

#import sys
#sys.stdin = open("sample_input.txt", "r")
p = int(input())
for a in range(0,p):
    n = input() #1
    value = int(n) #1
    data = [0] * 10 # 2
    while True: #3
        for i in range(len(n)): #3
            data[int(n[i])]+=1
        if not data.count(0) :
            print('#%d %d' % (a+1,int(n)))
            break
        
        n = str(value + int(n))


