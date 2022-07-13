#정수 3개를 공백두고 입력받아 합과 평균을 출력해보자.
#평균은 소숫점 이하 셋째 자리에서 반올림하여 둘째 자리까지 출력한다.
a,b,c = input().split()
a,b,c = int(a),int(b),int(c)
d=(a+b+c)/3
print(a+b+c)
print(format(d,'.2f'))