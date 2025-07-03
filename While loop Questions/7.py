#  Sum of cube of all even numbers from 1 to 100 with using function

def cubeven():
    sum=0
    i=1
    while(i<=100):
        if i%2==0:
            sum+=i**3
        else:
            pass
        i+=1
    print(sum)
cubeven() # 13005000

# # With return

def cubeven1():
    sum=0
    i=1
    while i<=100:
        if i%2==0:
            sum+=i**3
        else:
            pass
        i+=1
    return sum

Ce=cubeven1()
print(Ce) # 13005000