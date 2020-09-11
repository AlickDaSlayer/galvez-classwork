times_table = 0
valid_times_table = False # -- This variable will determine if the input is correct

while not valid_times_table: # -- Loop repeats until valid_times_table = True
    times_table = input("Enter a value from 1 to 20:   ")
    if times_table.isnumeric():
        times_table = int(times_table)
        if times_table > 0 and times_table < 21: # -- Range of the times_table
            columns = input("How many columns do you want?   ")
            if columns.isnumeric():
                columns = int(columns)
                for x in range(1, columns + 1):
                    print(times_table * x)
                    valid_times_table = True
                #Next
        else:
            print("Value is not in the correct range [1-20]")
        #End If
    else:
        print("The value is not valid")
    #End If
#End While
