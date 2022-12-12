def test(li):
    return all(i in range(1000) and abs(i - j)>= 10 for i in li for j in li if i != j) and len(set(li))
nums = list(range(0, 1000, 10))
print(test(nums))