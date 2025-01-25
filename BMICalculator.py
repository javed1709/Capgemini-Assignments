w=float(input("Enter the weight"))
h=float(input("Enter the height"))
bmi=w/h**2
if bmi<18.5:
    print("Body is Under-Weight")
elif bmi>=18.5 and bmi<=24.9:
    print("Body is Normal-Weight")
elif bmi>=25 and bmi<=29.9:
    print("body is Over-Weight")
