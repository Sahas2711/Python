def fact(num):
    if num == 0:
        return 1
    else:
        return num*fact(num-1)
a = int(input("Enter the number"))
print(fact(a))