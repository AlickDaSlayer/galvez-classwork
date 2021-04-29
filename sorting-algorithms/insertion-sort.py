import random

# -- INSERTION ALGORITHM -- #

def insertion_sort(arr):
    for i in range(1, len(arr)):
        currentValue = arr[i]
        currentPosition = i

        while currentPosition > 0 and arr[currentPosition - 1] > currentValue:
            arr[currentPosition] = arr[currentPosition - 1]
            currentPosition = currentPosition - 1
        #endwhile

        arr[currentPosition] = currentValue
    #next i
#endprocedure

# -- TEST ARRAY -- #

list = [] * 1000
for x in range(1000):
    list.append(random.randint(0, 1000))
#next x
print(list)

# -- INSERTION SORT -- #

insertion_sort(list)
print(list)