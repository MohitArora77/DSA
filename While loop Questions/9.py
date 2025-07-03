# Sum of Cube of all odd numbers from 1 to 100 with using function
def Cubeodd():
    sum=0
    i=1
    while i<=100:
        if i%2!=0:
            sum+=i**3
        else:
            pass
        i+=1
    print(sum)

Cubeodd() # 12497500

# # With Return

def cubeodd1():
    sum=0
    i=1
    while(i<100):
        if i%2!=0:
            sum+=i**3
        else:
            pass
        i+=1
    return sum

Co=cubeodd1()
print(Co) # 12497500