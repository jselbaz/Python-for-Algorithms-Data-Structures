def anagram(s1, s2):
        s1 = s1.lower().replace(' ','')
        s2 = s2.lower().replace(' ','')
        return sorted(s1) == sorted(s2)
        
def anagram2(s1, s2):
        s1 = s1.lower().replace(' ','')
        s2 = s2.lower().replace(' ','')
        
        if len(s1) != len(s2):
                return False
        
        count = {}
        
        for letter in s1:
                if letter not in count:
                        count[letter] = 1
                else:
                        count[letter] += 1
                        
        for letter in s2:
                if letter not in count:
                        count[letter] = 1
                else:
                        count[letter] -= 1
        
        for letter in count:
                if count[letter] != 0:
                        return False
        
        return True

print(anagram2('dog', 'god'))
print(anagram2('clint eastwood','old west action'))
print(anagram2('aa','bb'))
print(anagram2('go go go','gggooo'))
print(anagram2('abc','cba'))
print(anagram2('hi man','hi     man'))
print(anagram2('aabbcc','aabbc'))
print(anagram2('123','1 2'))
