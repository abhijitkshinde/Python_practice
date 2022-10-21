def hcf(a, b):
    if(b == 0):
        return a
    else:
        print(a%b)
        return hcf(b, a % b)


a = 24
b = 9

# prints 12
print("The gcd of a and b is : ", end="")
print(hcf(a, b))
