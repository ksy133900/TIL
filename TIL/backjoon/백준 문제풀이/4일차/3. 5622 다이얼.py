import sys
sys.stdin = open('다이얼.txt','r')


alpa = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
# 전화기 번호마다 짝지어져있는 알파벳들 묶어서 변수에 저장
word = input() # wa
# 대문자 입력받고
sec = 0
# 초 0으로 설정

for i in range(len(word)):
# 내가 입력한 문자의 길이만큼 반복 시작 ex) 'wa'면 2번

    for j in alpa:
    # alpa 리스트 순회
    
        if word[i] in j:
        # 내가 입력한 word[i]의 문자가 j에 있으면
        
            sec += alpa.index(j)+3 
            #sec에 alpa 인덱스 j의 값에 3을 더하고 저장한다.
 
 # alpa = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','#?  WXYZ']           
 #          0+3 , 1+3   2+3   3+3   4+3    5+3   6+3    #?  7+3
 #           3     4     5     6     7      8     9      #?  10

print(sec)
# 'W'=7+3=10
# 'A'=0+3=3
# 13