
import sys

sys.stdin = open("_괄호짝짓기.txt")

# 스택을 이용해보자
# 먼저 왼쪽 향한 괄호 4종류를 bracket_list 넣어준다.
# 순회하다가 오른쪽 괄호 종류 만나면 그 괄호와 짝이 맞는 왼쪽 괄호를 bracket_list에서 pop한다.
# 근데 뺄 왼쪽 괄호가 해당하는 짝의 괄호가 아니면 result=0으로 바꾸고 반복 종료
# 괄호 종류 4개니까 각 괄호마다 if문 넣어서 작성한다.
 
T = 10
for _ in range(1,T+1):
    C = int(input())
    bracket = list(input())
    bracket_list = []
    result = 1
    for i in bracket:
        if i == '(' or i == '[' or i == '{' or i == '<':
            bracket_list.append(i)
        if i == ')':
            if bracket_list.pop() != '(':
                result = 0
                break
        if i == ']':
            if bracket_list.pop() != '[':
                result = 0
                break
        if i == '}':
            if bracket_list.pop() != '{':
                result = 0
                break
        if i == '>':
            if bracket_list.pop() != '<':
                result = 0
                break
    print(f'#{_}',result)