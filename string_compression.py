def string_compress(s):
    r = ""
    l = len(s)
    i = 1
    cnt = 1
    
    while i < l:
        if s[i] == s[i-1]:
                cnt += 1
        else:
                r = r + s[i-1] + str(cnt)
                cnt = 1
        i += 1
    r = r + s[i-1] + str(cnt)
    return r
    
print(string_compress('AAAAABBBBCCCC'))
print(string_compress('AAAaaBBbbbCCCCc'))