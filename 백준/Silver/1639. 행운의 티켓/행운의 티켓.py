import sys


# 왼쪽 N자리 합과 오른쪽 N자리 합이 같은지 확인
def isLucky(x):
    mid = len(x) // 2
    sum1 = sum(x[:mid])
    sum2 = sum(x[mid:])
    if sum1 == sum2:
        return True
    else:
        return False

def solution(arr):
    if len(arr) % 2 == 0:
        chk = len(arr)
    else:
        chk = len(arr) - 1
    while chk > 0:
        i = 0
        ans = 0
        while i + chk <= len(arr):
            # 행운의 티켓이면 반복문 종료
            if isLucky(arr[i:i + chk]):
                ans = chk
                return ans
            i += 1
        chk -= 2
    return 0


s = list(map(int, list(sys.stdin.readline().strip())))
print(solution(s))