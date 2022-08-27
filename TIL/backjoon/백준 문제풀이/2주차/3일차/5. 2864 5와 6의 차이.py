import sys
sys.stdin = open("5와 6의 차이.txt", "r")
input = sys.stdin.readline

A , B = map(int,input().split())

C=str(A)  # C,D는 최솟값 (숫자 2개 다 5로 본 경우)
D=str(B)

E=str(A)  # E,f는 최댓값 (숫자 2개 다 6으로 본 경우)
F=str(B)

while '6' in C:
    C = C.replace('6','5')
while '6' in D:
    D = D.replace('6','5')
C=int(C)
D=int(D)

while '5' in E:
    E = E.replace('5','6')
while '5' in F:
    F = F.replace('5','6')
E=int(E)
F=int(F)

print(C+D,end=' ')
print(E+F)