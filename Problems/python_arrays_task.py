
def rev_func(input_value):
    letter = input_value[0]
    if len(input_value) == 1:
        return letter
    else:
        return rev_func(input_value[1:]) + letter
    #endif
#end function

print(rev_func('STAR'))
