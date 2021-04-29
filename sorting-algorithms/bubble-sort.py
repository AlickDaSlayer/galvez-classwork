import random

# -- SORTING FUNCTION -- #

def bubble_sort(arr):
    # We go through the list as many times as there are elements
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            #endif
        #next j
    #next i
#endprocedure

# -- TEST ARRAY -- #

list = [] * 1000
for x in range(1000):
    list.append(random.randint(0, 1000))
#next x
print(list)

# -- BUBBLE SORT -- #

bubble_sort(list)
print(list)