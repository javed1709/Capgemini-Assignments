lst=[]
odd,even=[],[]
n=int(input("Enter the size of array:"))
for i in range(0,n):
    x=int(input("Enter the value:"))
    lst.append(x)
for i in lst:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(f"Even List:{even}")
print(f"Odd List:{odd}")
