def fub_n(n):
    if n == 0:
        return 0
    if n == 1:

        return 1
    
    return fub_n(n-1)+fub_n(n-2)


print(fub_n(80))