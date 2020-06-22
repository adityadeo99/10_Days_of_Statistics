def median(nums):
    # nums.sort()
    n = len(nums)
    mid, o = divmod(n, 2)
    if o:
        return nums[mid]
    else:
        return int((nums[mid] + nums[mid-1])/2)

n = int(input())
n2 = int(n/2)
nums = sorted(list(map(int, input().split())))
print(median(nums[:n2]))
print(median(nums))
print(median(nums[-n2:]))
