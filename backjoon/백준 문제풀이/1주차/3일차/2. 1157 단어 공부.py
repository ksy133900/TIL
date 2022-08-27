x=input().upper() # baaa 처음부터 대문자 할당

word=list(set(x)) # [b,a]
result=[]

for i in word:
    a = x.count(i) # 'BAAA'에서 B,A 문자를 골라 카운트 해서 a에 할당
    result.append(a) # result 리스트에 [1,3] 삽입
    
if result.count(max(result)) > 1:
    #! result 리스트에서 가장 큰 값(max(result)을 count()함수로 셌을 때
    #! 최댓값이 1보다 큰 경우(2개 이상 최댓값이 존재할 경우)    
       print('?') #! ?를 출력한다.
            
else:  # 겹치는 게 없는 경우 (최댓값이 1개)
    
    max_index=result.index(max(result))
    # result = [1,3] 최댓값이 3이므로 1번 인덱스를 가져옴 max_index=1
    
    print(word[max_index])
    # word[max_index] == word[1] = [B , A]에서 A
    # A
    