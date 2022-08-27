#두 정수(a, b)를 공백을 두고입력받아
#a와 b의 값이 같으면 True 를, 같지 않으면 False 를 출력
a,b=input().split()
a,b= int(a),int(b)
if a==b:
    print('True')
else:
    print('False')