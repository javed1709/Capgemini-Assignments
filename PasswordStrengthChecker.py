s=input("Enter the string:")
uc,lc,spc,dgi=0,0,0,0
chk=False
for i in s:
    if len(s)<8:
        print("Password should be atleast length 8 long")
        chk=True
        break
    elif i>='A' and i<='Z':
        uc +=1
    elif i>='a' and i<='z':
        lc +=1
    elif i>='0' and i<='9':
        dgi +=1
    else:
        spc +=1
if uc==0:
    print("There should be Atleast one Uppercase character")
    chk=True
if lc==0:
    print("There should be Atleast one lowercase character")
    chk=True
if dgi==0:
    print("There should be Atleast one Digit")
    chk=True
if spc==0:
    print("There should be Atleast one special character")
    chk=True
if chk:
    print("Password Not Accepted, Make it strong in above factors")
else: print("Password Accepted!")





    

