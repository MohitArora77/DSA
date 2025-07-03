#  Sum of square of all odd numbers from 1 to 100 with using function

def oddsq():
    sum=0
    i=1
    while (i<=100):
        if i%2!=0:
            sum+=i**2
        else:
            pass
        i+=1
    print(sum)
    
oddsq() # 166650

def oddsq1():
    sum=0
    i=1
    while (i<=100):
        if i%2!=0:
            sum+=i**2
        else:
            pass
        i+=1
    return sum

Os=oddsq1()
print(Os) # 166650