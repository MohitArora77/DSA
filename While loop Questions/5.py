# Ques -> Sum of cube of all natural number from 1 to 100 using function (without return statement)

def cubenum():
    sum=0
    i=1
    while (i<=100):
        sum+=i**3
        i+=1
    print(sum)
    
cubenum() # 25502500

# # With Return
def cubenum1():
    sum=0
    i=1
    while (i<=100):
        sum+=i**3
        i+=1
    return sum

cubenumber=cubenum1()
print(cubenumber) # 25502500