nums = [1, 2, 2, 3, 4, 5, 5, 5]

count = 1
for i in range(1, len(nums)):
    if nums[i - 1] != nums[i]:
        count += 1;

print(count)
