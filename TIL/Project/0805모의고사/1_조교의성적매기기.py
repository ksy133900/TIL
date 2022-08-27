import sys
sys.stdin = open("_조교의성적매기기.txt")
# 문제에 점수가 내림차순으로 나열되어있음. 
# 학생의 시험,과제점수로 총점 계산해준 뒤 "정렬 전에" T(점수 보고 싶은 학생)의 점수 값을 저장함
# 학생 점수를 내림차순으로 정렬을 해준다.
# N/10명의 학생에게 동일한 점수 부여 가능 (equal 변수 생성
# 내림차순으로 정렬한 score 리스트에, k의 점수 값에 해당하는 "인덱스 값"을, equal로 나눠 그 몫을 result에 저장
# test_score의 result 값을 문자로 출력한다. ex) test_score[2] = 'A-'

test_score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
T = int(input())
for _ in range(1,T+1):
    N,K = map(int,input().split())
    score = []
    for i in range(N):
        a, b, c = map(int, input().split())
    
        total_score = (a * 0.35) + (b * 0.45) + (c * 0.2)
        score.append(total_score)
        
    k_jumsu = score[K-1]
    print(k_jumsu)
    score.sort(reverse=True)
    
    equal = N // 10
    result = score.index(k_jumsu) // equal
    print(result)
    print("#%d %s" % (_, test_score[result]))
    
    
    
    