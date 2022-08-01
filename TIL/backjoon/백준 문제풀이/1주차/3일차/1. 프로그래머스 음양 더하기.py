def solution(absolutes, signs):
    # sings 가 참이면 해당 absoluted은 실제 정수가 양수, 거짓이면 음수 
    # 주어진 수에 하나씩 접근
    # 양수, 음수가 적용된 실제 합
    answer = 0
    for i in range(len(absolutes)):
        # 참인 경우 정수이므로 더하기 
        if signs[i]:
            answer += absolutes[i]
            # 거짓인 경우 음수임으로 빼기
        else:
            answer -= absolutes[i]
    return answer

print(solution([4, 7, 12],[True, False, True]))
print(solution([1, 2, 3],[False, False, True]))