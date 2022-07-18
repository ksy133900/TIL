#numbers = input().split()
#print(sum(numbers))

## TypeError로 타입이 다르기 때문에 합계 출력이 불가능(int형과 str형)

numbers = map(int,input().split())
print(sum(numbers))

#map함수를 이용하여 내부의 있는 요소들을 int형 변환 한다.
