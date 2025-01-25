lst=[]
n=int(input("Enter the siz eof array:"))
for i in range(0,n):
    x=int(input("Enter the value:"))
    lst.append(x)

mx1,mx2=0,0
for i in lst:
    if i>mx1:
        if(mx2==0): mx2=i
        else: mx2=mx1
        mx1=i

print(f"Second Max odf list is {mx2}")