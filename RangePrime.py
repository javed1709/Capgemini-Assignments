def is_prime(n):
    i=2
    while ((i*i))<=n:
        if n%i==0:
            return False
        i +=1
    return True

def PrintPrimesInRange(n):
    for i in range(2,n+1):
        if is_prime(i):
            print(i)

n=int(input("Enter number:"))
PrintPrimesInRange(n)