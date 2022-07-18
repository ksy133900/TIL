#아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 
#코드에서 오류를 찾아 원인을 적고, 수정하세요.
word = "HappyHacking"
count = 0
for char in word:
    if char == "a" or "e" or "i" or "o" or "u":
        count += 1
print(count)

#if문에서 복수의 조건이 필요하다면
#elif문 이용해서 하나씩 넣어줍시다...

word = "HappyHacking"
count = 0
for char in word:
    if char == "a" :
        count += 1
    elif char == 'e':
        count += 1
    elif char == 'i':
        count += 1
    elif char == 'o':
        count += 1
    elif char == 'u':
        count += 1
print(count)