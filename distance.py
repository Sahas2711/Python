def dist(x1,x2,y1,y2):
    a  = x2 - x1
    a = a*a
    b = y2 - y1
    b = b*b
    c = a+b
    return c ** 0.5

a = int(input("Enter the number"))
b = int(input("Enter the number"))
c = int(input("Enter the number"))
d = int(input("Enter the number"))
print(dist(a,b,c,d))