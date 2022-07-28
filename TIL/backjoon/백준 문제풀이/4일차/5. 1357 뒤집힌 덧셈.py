X,Y = map(int,input().split())
r = str(X) 
s = str(Y)

a = r[::-1]
b = s[::-1]
# 각 변수 r,s를 슬라이싱해서 역순으로 배치하고 a,b에 저장

k = int(a)
p = int(b)
# a,b를 문자열에서 정수로 변환 후 k,p에 각각 저장

l = k+p
m = str(l)
u = m[::-1]
# k+p를 l에 저장 후에  문자열로 변환해서 m에 저장,
# m을 슬라이싱해서 역순 배치 후 u에 저장
print(u)