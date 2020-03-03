def longest(s1, s2):
    a = s1 + s2
    b = ''.join(sorted(set(a)))
    return b