def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    d=dict()
    for char1 in str1:
        if char1 in d:
            d[char1] += 1
        else:
            d[char1] = 1
    for char2 in str2:
        if char2 not in d:
            return False
        else:
            if d[char2]==0:
                return False
            d[char2]-=1
    return True

print(is_permutation("abc","aaa"))