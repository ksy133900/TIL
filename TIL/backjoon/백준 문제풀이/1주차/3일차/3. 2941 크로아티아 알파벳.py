

alpa = (input()) #단어 입력
croa = ['c=','e' ,'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=','a','k']

for i in croa: # croa 리스트 for문 순회
    #! croa 내 리스트 단어가 주어진 단어에 있으면 '~'로 교체해준다.
    #! replace(i,' ')에서  ' ' 내부는 문자 하나이기만 아무거나 써도 OK
    alpa = alpa.replace(i,'~') 
    
    print(alpa) # '~~~~~~'
print(len(alpa)) # 문자열의 길이 출력 = 6

