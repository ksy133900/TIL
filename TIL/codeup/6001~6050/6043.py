#실수 2개(f1, f2)를 공백으로 구분하여 입력받아f 1 을 f2 로 나눈 값을 출력.
#이 때 소숫점 넷째자리에서 반올림하여 무조건 소숫점 셋째 자리까지 출력한다.
f1,f2=input().split()
f1=float(f1)
f2=float(f2)
c=f1/f2
print(format(c,'.3f'))

