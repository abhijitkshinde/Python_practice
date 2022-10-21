def find_sum_until_n(n):

    if n == 1:
        return 1

    sum_r = n + find_sum_until_n(n -1 )
    # sum_i = 0
    # for i in range(n+1):
    #     sum_i += i
    
    return sum_r

print(find_sum_until_n(100))