def reverse(s):

    if len(s) <= 1:
        return s
        
    return reverse(s[1:]) + s[0]
    
print(reverse('abc'))
print(reverse('hello'))
print(reverse('hello world'))
print(reverse('123456789'))