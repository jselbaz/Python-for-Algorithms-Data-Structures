def unique_chars(s):
    l = len(s)
    i = 1
    while i < l:
        if s[i] == s[i-1]:
                return False
        else:
                i += 1
    return True
    
def unique_chars2(s):
        return len(set(s)) == len(s)
    
print(unique_chars("abcde"))  #t
print(unique_chars("abcdee")) #f
print(unique_chars("")) #t
print(unique_chars("goo")) #f