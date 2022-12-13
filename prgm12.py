def test(strs):
    return [s == s[::-1] for s in strs]
strs = ['palindrome', 'madamimadam', '', 'foo', 'eyes']
print("original strings:")
print(strs)
print("\nTest whether the given strings are pa;indromes or not:")
print(test(strs))