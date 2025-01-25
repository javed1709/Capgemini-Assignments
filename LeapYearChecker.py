def leap_year(n):
    return (n%400==0 and n%100!=0 or n%4==0)

n=int(input("Enter the no of Queries to Process:"))

for i in range(0,n):
    yr=int(input("Enter the Year:"))
    if leap_year(yr):
        print(f"Given Year {yr} is a Leap Year")
    else:
        print(f"Given Year {yr} is not a Leap Year")

