nums = [5, 7, 7, 8, 8, 10]
target = 7
start = -1
end = -1
for i in range(len(nums)):
    if nums[i] == target:
        if start == -1:
            start = i
        end = i
result = [start, end]
print(result)
