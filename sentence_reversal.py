def rev_word(s):

        words = []
        length = len(s)
        spaces = [' ']
        i = 0
        while i < length:
                if s[i] not in spaces:
                        word_start = i
                        while i < length and s[i] not in spaces:
                                i += 1
                        words.append(s[word_start:i])
                i += 1
        return " ".join(reversed(words))

print(rev_word('          space before'))
print(rev_word('Hi John,    are you ready to go?'))
print(rev_word('Hello John,    how are you '))