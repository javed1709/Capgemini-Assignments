def say(s):
    i,j=0,len(s)-1
    while i<=j:
        if s[i]!=s[j]:
            return False
        i +=1
        j -=1
    return True

s=input("Enter the string:")
if say(s):
    print(f"Given String {s} is a Palindrome")
else:
    print(f"String {s} is not a palindrome")