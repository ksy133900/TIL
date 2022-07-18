# len함수의 경우 문자열의 길이를 구하는 함수인데
# numbers는 int형이네요

number = '22020718'
print(len(number))

#22020718 -> '22020718' 문자열 변환을 해주면 될 것 같습니다.

#또는 다른 방법이 있습니다.

def iter_size(numbers):
    cnt=0
    while numbers:
        numbers//=10
        cnt+=1
    return cnt
print(iter_size(22020718))

## iter_size()함수를 이용해 print()에 있는 숫자를 호출하고
## 10으로 나누어 질 때마다 cnt를 1씩 증가시키며
#몫이 0이 될떄까지 반복한다.
