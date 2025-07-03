# Factorial of that number (input from user)

def fact(n):
    fact=1
    i=1
    while(i<=n/2):
        if (n%i==0):
            fact*=i
        i+=1
    print(fact)
fact(20)
    