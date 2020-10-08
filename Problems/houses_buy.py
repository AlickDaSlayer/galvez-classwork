
cases_T = int(input())
case_count = 0

while case_count < cases_T:
    case_count  += 1
    houses_N, dollars_B = [int(x) for x in input().split()]
    house_list = [int(x) for x in input().split()]
##    house_list.sort()

print(cases_T, houses_N, dollars_B)
