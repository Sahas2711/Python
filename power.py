def pow(a,b):
    if b == 0:
        return 1
    else:
        return a*pow(a,b-1)
a = int(input("Enter the base number"))
b = int(input("Enter the power"))
print(pow(a,b))