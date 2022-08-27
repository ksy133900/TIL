#문자열 word가 주어질 때, 
# 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
word = 'banana' 
cnt=0
idx = -1
for i in word:
    if i == 'a':
        idx = cnt
        break
    cnt += 1
print(idx)

#테스트 케이스 'apple'
word = 'apple' 
cnt=0
idx = -1
for i in word:
    if i == 'a':
        idx = cnt
        break
    cnt += 1
print(idx)

##테스트 케이스 'kiwi'
word = 'kiwi' 
cnt=0
idx = -1
for i in word:
    if i == 'a':
        idx = cnt
        break
    cnt += 1
print(idx)

#추가문제
word = 'HappyHacking' 
cnt=0
idx = -1
for i in word:
    if i == 'a':
        idx = cnt
        print(idx,end=' ')
    cnt += 1
