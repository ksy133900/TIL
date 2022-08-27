#가로와 세로의 길이를 각각 a, b로 받아 사각형 넓이와 둘레를 함께 반환하는 함수 rectangle을 정의하시오. 
#사각형이 가로가 20, 세로가 30일 때의 결과를 출력하시오.
a=20
b=30
def rectangle(x,y):
    return x*y,2*(a+b)
result=rectangle(a,b)
print(result)