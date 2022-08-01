problem = []

while True:
    a = input()
    if a == '문제':
        problem.append(1)
    elif a == '고무오리':
        if not problem :
            problem.append(1)   
            problem.append(1)
        else :
            problem.pop()
    
    elif a == '고무오리 디버깅 끝':
        break
    
if not problem:
    print('고무오리야 사랑해')
else :
    print('힝구')
    
