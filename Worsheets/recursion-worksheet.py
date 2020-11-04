
def calcSum(n):
    if n == 0:
        return n
    else:
        return n + calcSum(n - 2)
    #end if
#end function

sum = calcSum(10)
print("sum = ", sum)

input("\nPress Enter to exit program.  ")

### SRC - I'd like to see the comparision timings between
### iterative and recursive solutions...
