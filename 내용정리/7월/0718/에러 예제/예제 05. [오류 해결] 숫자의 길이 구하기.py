# len함수의 경우 문자열의 길이를 구하는 함수인데
# numbers는 int형이네요
# 문자열 변환이 필요할 것 같습니다.
number = '22020718'
print(len(number))

#또는

number = 22020718
print(len(str(number)))

#또는 다른 방법이 있습니다.

numbers = 22020718
cnt=0
while numbers: #<= int:0이 아닌 수면 무조건 true! 0이면 false
    numbers//=10
    cnt+=1        
print(cnt)
##ex) 123 = 100+20+3 = 1x100+2x10+3x1
## 10으로 나누어 질 때마다 cnt를 1씩 증가시키며
#몫이 0이 될떄까지 반복한다.
