word='banana'
dic={} # 빈 딕셔너리를 만든다

for i in word: # for 문에 리스트가 아닌 문자열을 넣으면 변수에 문자열의 
               # 각 문자가 하나씩 차례대로 대입되어 코드가 실행된다.
    if i in dic: # 문자가 딕셔너리에 있으면 1을 더하고 없으면 새로 추가한다.
        dic[i]=dic[i]+1
    else:
        dic[i]=1
print(dic)
        