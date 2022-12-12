def test(nums):
    return all([sum(nums[:i]) == i for i in range(len(nums))])
nums = [2, 2, 2, 2, 2]
print(test(nums))