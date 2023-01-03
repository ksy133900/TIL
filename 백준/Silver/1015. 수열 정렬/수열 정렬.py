import sys

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

index = [-1] * n

for i in range(n):
    idx = nums.index(min(nums))
    index[idx] = i
    nums[idx] = 1001

print(' '.join(map(str, index)))