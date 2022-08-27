#평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력
#영문자 1개가 입력된다.
#A : best!!!
#B : good!!
#C : run!
#D : slowly~
#나머지 문자들 : what?
x=input()
if x == 'A':
    print('best!!!')
elif x=='B':
    print('good!!')
elif x=='C':
    print('run!')
elif x=='D':
    print('slowly~')
else:
    print('what?')