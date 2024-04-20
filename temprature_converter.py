def far(n):
    return 32+(5/9)*n
def kel(n):
    return 273+n
cel=int(input("Enter the temprature in degree celcius"))
print(f"{far(cel)} is the temprature after conversion in farahnite")
print(f"{kel(cel)} is the temprature after conversion in kelvin")
