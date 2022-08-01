# 아래 코드는 리스트에서 최댓값을 구하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.


    #max() 예약어를 변수명으로 사용 하였기 때문이다
    #max를 변수명으로 사용한 후에 max()함수를 다시 사용했으니 이름 중복으로
    #오류가 발생한다.
    #max = max(number_list) 앞에 변수명의 max를 다른 변수명으로 바꿔주자
    
number_list = [1, 23, 9, 6, 91, 59, 29]
max1 = max(number_list)

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max2 = max(number_list2)

if max1 > max2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")
elif max1 < max2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")
else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")