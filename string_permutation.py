def permute(s):
        output = []
        
        if len(s) == 1:
                output = [s]
                
        else:
                for i,letter in enumerate(s):
                        for permutation in permute( s[:i] + s[i + 1:]):
                                output += [letter + permutation]
                                
        return output