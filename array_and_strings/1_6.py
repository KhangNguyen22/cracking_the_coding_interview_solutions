def compress(s):
    out = ""
    sum = 1
    l = len(s)
    for idx in range(l):
        if idx == l-1 or s[idx] != s[idx+1]:
            out = out + s[idx] + str(sum)
            sum = 1
        else:
            sum += 1
    print(out)
    return out if (len(out) < l) else s


print(compress("aabcccccaaa"))