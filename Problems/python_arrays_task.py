
def rev_word(word):
    letter = word[0]
    if len(word) == 1:
        return letter
    else:
        return rev_word(word[1:]) + letter
    #endif
#end function

print(rev_word('STAR'))
