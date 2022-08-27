# from pprint import pprint
# matrix = []
# for _ in range(3):
#     #a = list(map(int,input().split()))
#     #matrix.append(a)
#     matrix.append(list(map(int,input().split()))) #위 4,5라인의 코드와 동일
# pprint(matrix)

matrix2 = [list(map(int,input().split())) for _ in range(3)]
print(matrix2)