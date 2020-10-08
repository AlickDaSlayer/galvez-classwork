
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

## -- How to create an array in Python -- ##

my_array_list = []
for i in range(10):
    my_array_list.append(0)

print(my_array_list)

# -- OR -- #

my_array_list = [0 for x in range(10)]
print(my_array_list)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

## -- 2D Arrays in Python -- ##

my_array_list = [[1,2,3] for x in range(10)]
print(my_array_list)

print(my_array_list[3][2])

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

## -- Tuples in Python -- ##

my_tuple = (1, 2, 3)
print(my_tuple[2])

string_tuple = ('c', 'a', 't')

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# -- String slicing -- #

my_string = 'impossible'
my_string = my_string[0:3] + '0' +  my_string[4:10] # - This needs the value of the index after but not including
# -- my_string[4::2] <-- has a step of +2  
print(my_string)
