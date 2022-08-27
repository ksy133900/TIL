N = int(input())
number = list(map(int,input().split()))
number.sort()
index=(N-1)//2
print("{}".format(number[index]))
