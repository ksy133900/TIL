#공백 구분 정수 a, b, c 중 가장 작은 값을 출력
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
d= a if a<b  else b # a와 b를 비교했을 때 b가a보다 크면 d에 a를 넣기 그게 아니면(a가 b보다 크면) b를 넣는다.
e= d if d<c  else c # a와 b를 비교한 값을 c랑 비교한다. c가 d보다 크면 e에 c값을 넣는다. 아니면 d를 넣음 
print(e)
