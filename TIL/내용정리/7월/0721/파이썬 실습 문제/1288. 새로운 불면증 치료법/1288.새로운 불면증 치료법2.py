T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    N1 = N
    numbers = set()  #set에 계속 추가 예정
    while True:
        for n in str(N):
            numbers.add(n)  #number set에 추가
        if len(numbers) == 10:
            break
        N += N1
    print('#%d %d'% (test_case,N))