def test(strs, prefix):
    return [s for s in strs if s.startswith(prefix)]
strs = ['cat', 'car', 'fear', 'center']
prefix = "ca"
print(strs)
print("starting prefix:", prefix)
print(test(strs, prefix))