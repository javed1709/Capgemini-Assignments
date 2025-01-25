def randomnumber(l,h):
    chk=True
    print("You Have five chances to guess the number")
    cnt=0
    mid=l+(h-l)/2
    while l<=h:
        if cnt==5: break
        mid=l+(h-l)/2
        if chk:
            print("Number is too high")
            l=mid-1
            chk=False
        else:
            print("Number is too low")
            h=mid+1
            chk=True
        cnt +=1

randomnumber(1,100)

