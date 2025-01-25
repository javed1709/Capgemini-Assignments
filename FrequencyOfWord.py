frq={}
s=input("Enter the string string:").split(" ")
print(s)
for i in s:
    if i in frq.keys():
        frq[i] +=1
    else:
        frq[i]=1
for i in frq:
    print(f"{i} occurs {frq[i]} times")