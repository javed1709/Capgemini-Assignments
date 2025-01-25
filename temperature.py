def celcius(temp):
    return (5/9*(temp-32))
def kelvin(temp):
    return (5/9*(temp+459.67))
def fahrenheit(temp):
    return ((9/5)*temp+32)

fh=int(input("Enter temperature in Fahrenheit"))
cl=int(input("enter temperature in celcius"))
print(f"temperature in celcius {celcius(fh)} , temperature in kelvin {kelvin(fh)}")
print(f"temperature in Fahrenheit {fahrenheit(cl)}") # finding the Fahrenheit using celcius