import sys
sys.stdin = open("숫문영.txt", "r")

s = input() # 문자 입력받기
numbers = {
    'zero':'0',
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
}
print(numbers.items()) # => 딕셔너리의 키,값을 묶어서 튜플로 반환

for i in numbers.items(): 
#1 i = ('zero','0') => i[0] = 'zero' , i[1] = '0'
#2 i = ('one' ,'1') => i[0] = 'one'  , i[1] = '1'...순회

     s = s.replace(i[0], i[1])
# s에 있는 문자에 i[0]에 해당하는 문자가 있으면,
# i[0]을 i[1]로 replace 합니다. ex) 'one' => '1' 결과를 s에 저장
print(s)