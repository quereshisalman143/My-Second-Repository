def test(strl):
    return strl[len(strl)-2] in strl[len(strl)-1] and strl[len(strl)-2] != strl[len(strl)-1]

strl = ['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']
print(test(strl))