
def calc(n):
    if n == 0:
        return 1
    else:
        return n * calc(n-1)
    #end if
#end function

print(calc(0))
print(calc(4))
print(calc(5))
