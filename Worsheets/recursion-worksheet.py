
def calcSum(n):
    if n == 0:
        return n
    else:
        return n + calcSum(n - 2)

sum = calcSum(10)
print("sum = ", sum)

input("\nPress Enter to exit program.  ")
