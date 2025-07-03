# Ques -> Sum of square of all natural number from 1 to 100 using function (without return statement)

def sqnum():
    sum=0
    i=1
    while (i<=100):
        sum+=i**2
        i+=1
    print(sum)
    
sqnum() # 338350

# # With Return

def sqnum1():
    sum=0
    i=1
    while (i<=100):
        sum+=i**2
        i+=1
    return sum

sq=sqnum1()
print(sq) # 338350