def tri(a,b):
    return (a*b)/2
def rect(a,b):
    return (a*b)
a = int(input("Enter the bsse of traingle"))
b = int(input("Enter the height of traingle"))
print(f"{tri(a,b)} is the area of traingle")
num1 = int(input("Enter the bsse of rectangle"))
num2 = int(input("Enter the height of rectangle"))
print(f"{tri(num1,num2)} is the area of rectangle")
n=int(input("Enter the side of square"))
print(n*n," is the area of square")