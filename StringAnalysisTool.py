def reverse(s):
    ans=""
    i=len(s)-1
    while i>=0:
        ans +=(s[i])
        i -=1
    return ans
vow,conso,dig,special_characters=0,0,0,0
s=input("Enter the string:")
for i in s.lower():
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        vow +=1
    elif (i>='a' and i<='z' and i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        conso +=1
    elif (i>='0' and i<='9'):
        dig +=1
    else:
        special_characters +=1

print(f"Vowels: {vow}")
print(f"Consonants: {conso}")
print(f"Digits: {dig}")
print(f"Special Characters: {special_characters}")
print(f"Reverse of string:{reverse(s)}")